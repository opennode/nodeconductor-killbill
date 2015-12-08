Invoices
--------

To get a list of invoices, run GET against **/api/killbill-invoices/** as an authenticated user.

Filtering of invoices is supported through HTTP query parameters, the following fields are acceptable:

- ?customer=<customer uuid>
- ?month=<month>
- ?year=<year>


Invoice PDF
-----------

PDF version of invoice is available with GET against **/api/killbill-invoices/<invoice_uuid>/pdf/**.
In order to force browser to download and save PDF use **?download=1** parameter.


Invoice items
-------------

To get items of invoice run GET against **/api/killbill-invoices/<invoice_uuid>/items/**.


Invoices amount for customers
-----------------------------

PDF version of invoices sum for all customers is available against **/api/killbill-invoices/annual_report/**.
To group invoices by month use **?group_by=month** parameter. Otherwise they will be grouped by customers.
In order to force browser to download and save PDF use **?download=1** parameter.
