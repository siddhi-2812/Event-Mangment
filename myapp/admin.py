from django.contrib import admin
from .models import *

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def export_to_pdf(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['User_Id', 'Category', 'subcat','Package','First_Name','date','Location']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.User_Id, obj.Category, obj.subcat,obj.Package,obj.First_Name,obj.date,obj.Location])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to PDF"

def export_to_pdf2(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['Name', 'email', 'contactno']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.Name, obj.email, obj.contactno])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to PDF"

# Register your models here.

class show_user(admin.ModelAdmin):
    list_display = ["Name","contactno","email","password"]
    actions = [export_to_pdf2]
admin.site.register(User,show_user)


class show_category(admin.ModelAdmin):
    list_display = ["cat_name"]
admin.site.register(category,show_category)

class show_sub_category(admin.ModelAdmin):
    list_display = ["Category_Id","name"]
admin.site.register(sub_category,show_sub_category)    

class show_package(admin.ModelAdmin):
    list_display =["name","subcat_id","details","amount"]
admin.site.register(package,show_package) 

class show_booking(admin.ModelAdmin):
    list_display =["User_Id","Category","subcat","Package","First_Name","Last_Name","Phone_no","Time","Email","date","details","Location","timestamp"]
    list_filter = ['timestamp']
    actions = [export_to_pdf]
admin.site.register(BOOKING,show_booking)


class show_contact(admin.ModelAdmin):
    list_display = ["Name","Email","Subject","Message"]
admin.site.register(contact,show_contact)

class show_card(admin.ModelAdmin):
    list_display=["User_Id","Name","card_num","Cvv","Expiry_Date","timestamp"]
admin.site.register(Card,show_card)