import chargebee
import json
from django.http import HttpResponse

site_api_key = "test_Pv8CNcdT9OVj5cd0myD0GWu9cdXj3U91l2M"
site = "chinuki-test"

chargebee.configure(site_api_key,site)
# result = chargebee.Addon.retrieve({
#     "id" : "sms_pack",
#     "name" : "Sms Pack",
#     "invoice_name" : "sample data pack",
#     "charge_type" : "recurring",
#     "price" : 200,
#     "period" : 1,
#     "pricing_model" : "flat_fee",
#     "period_unit" : "month"
#     })
result = chargebee.Item.retrieve({
"id" : "one"

})
addon = result.addon

print("Result:...................",result)