from django.contrib import admin
from .models import Order, OrderItem
import datetime
import csv
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']

def export_to_csv(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; \ filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)
	fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	writer.writerow([field.verbose_name for field in fields])
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d/%m/%Y')
			data_row.append(value)
		writer.writerow(data_row)
	return response
export_to_csv.short_description = 'Export to CSV'


def order_pdf(obj):
	return mark_safe('<a href="{}">PDF</a>'.format(reverse('orders2:admin_order_pdf', args=[obj.id])))
order_pdf.short_description = 'PDF bill'

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'user','first_name','last_name','email',
					'created', 'updated',order_pdf,]
	list_filter = ['created', 'updated']
	inlines = [OrderItemInline]
	actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)