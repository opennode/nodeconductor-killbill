from django.apps import AppConfig
from django.db.models import signals
from django_fsm.signals import post_transition


class KillBillConfig(AppConfig):
    name = 'nodeconductor_killbill'
    verbose_name = "NodeConductor KillBill"

    def ready(self):
        from nodeconductor.structure import models as structure_models
        from nodeconductor.core.handlers import preserve_fields_before_update

        from . import handlers

        Invoice = self.get_model('Invoice')

        signals.post_save.connect(
            handlers.log_invoice_save,
            sender=Invoice,
            dispatch_uid='nodeconductor_killbill.handlers.log_invoice_save',
        )

        signals.post_delete.connect(
            handlers.log_invoice_delete,
            sender=Invoice,
            dispatch_uid='nodeconductor_killbill.handlers.log_invoice_delete',
        )

        for index, resource in enumerate(structure_models.PaidResource.get_all_models()):
            post_transition.connect(
                handlers.subscribe,
                sender=resource,
                dispatch_uid='nodeconductor_killbill.handlers.subscribe_{}_{}'.format(
                    resource.__name__, index),
            )

            signals.post_delete.connect(
                handlers.unsubscribe,
                sender=resource,
                dispatch_uid='nodeconductor_killbill.handlers.unsubscribe_{}_{}'.format(
                    resource.__name__, index),
            )

            signals.pre_save.connect(
                preserve_fields_before_update,
                sender=resource,
                dispatch_uid='nodeconductor_killbill.handlers.preserve_fields_before_update_{}_{}'.format(
                    resource.__name__, index),
            )

            signals.post_save.connect(
                handlers.update_resource_name,
                sender=resource,
                dispatch_uid='nodeconductor_killbill.handlers.update_resource_name_{}_{}'.format(
                    resource.__name__, index),
            )

        signals.post_save.connect(
            handlers.update_project_name,
            sender=structure_models.Project,
            dispatch_uid='nodeconductor_killbill.handlers.update_project_name',
        )

        signals.post_save.connect(
            handlers.update_project_group_name,
            sender=structure_models.ProjectGroup,
            dispatch_uid='nodeconductor_killbill.handlers.update_project_group_name',
        )
