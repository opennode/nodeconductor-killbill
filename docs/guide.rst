Billing integration
-------------------

NodeConductor can integrate with billing systems and expose typical features via REST API and admin interface.
At the moment, only KillBill_ is supported as a backend. The following features are available:

- Pushing chargeback information from the services for invoice generation (based on resource and license consumption).
  Usages of resources is accounted on an hourly basis.
- Getting invoice data from the backend.
- Propagating price lists to the backend.


.. _KillBill: https://killbill.io/

Configuration of integration with KillBill
++++++++++++++++++++++++++++++++++++++++++

Connecting NodeConductor with KillBill means defining KillBill API endpoint along with user credentials that have admin
access. API access for the NodeConductor service must be enabled in KillBill before connection can be established.

To setup a KillBill integration, add a billing block of configuration as shown in the example below.

.. code-block:: python

    # Example of settings for billing using KillBill API.
    NODECONDUCTOR['BILLING'] = {
        # url of billing API
        'api_url': 'http://killbill.example.com/1.0/kb/',
        # credentials
        'username': 'admin',
        'password': 'password',
        # tenant credentials
        'api_key': 'bob',
        'api_secret': 'lazar',
        # extra options
        'currency': 'USD',
    }

Synchronisation with product prices of KillBill
+++++++++++++++++++++++++++++++++++++++++++++++

NodeConductor can populate its price list based on the configured products in KillBill.

The following conventions are in place:

- KillBill product names and descriptions are taken as price list item names in NodeConductor.
- KillBill hourly price is taken as an item price.
