# -*- coding: utf-8 -*-
#!/usr/bin/env python
from .models import *
from reportlab.platypus import PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import A4, inch
import reportlab.rl_config

reportlab.rl_config.warnOnMissingFontGlyphs = 0


class MyPrint:
    def __init__(self, buffer):
        self.buffer = buffer


    def generate_report_programmes(self, programme_name):
        buffer = self.buffer

        #font
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=15)
        pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
        pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
        pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
        pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

        table_data = []
        elements = []
        reports = []

        table_data[:] = []
        order = 1

        table_data.append(["Broj indeksa", "Ime i prezime"])
        students = Student.objects.all().order_by('last_name')
        for student in students:
            if student.programme_of_study.name == str(programme_name):
                table_data.append([str(student.index), str(student)])

        if len(table_data) > 1:
            table_with_style = Table(table_data, [1.5 * inch, 3 * inch, 0.5 * inch])
            table_with_style.setStyle(TableStyle([
                ('FONT', (0, 0), (-1, -1), 'Vera'),
                ('FONTSIZE', (0, 1), (1, 0), 10),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                ('ALIGN', (0, 0), (1, 0), 'LEFT'),
            ]))
            elements.append(table_with_style)
            elements.append(PageBreak())
            reports.extend(elements)
            elements[:] = []
        else:
            elements[:] = []

        doc.build(reports)
        pdf = buffer.getvalue()
        buffer.close()
        
        return pdf



    def generate_report_employee(self, sortId):
        buffer = self.buffer

        #font
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=15)
        pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
        pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
        pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
        pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

        
        table_data = []
        elements = []
        reports = []

        table_data[:] = []
        order = 1


        if sortId == 1:
            table_data.append(["Redni\nbroj", "Ime i prezime"])
            employees = Employee.objects.all().order_by('last_name')
            for employee in employees:
                table_data.append([str(order) + ".", str(employee)])
                order += 1

        elif sortId == 2:
            table_data.append(["Redni\nbroj", "Ime i prezime", "Zvanje"])
            employees = Employee.objects.all().order_by('occupation')
            for employee in employees:
               table_data.append([str(order) + ".", str(employee), employee.occupation])
               order += 1

       
        if len(table_data) > 1:
            table_with_style = Table(table_data, [0.5 * inch, 3 * inch, 2.5 * inch])
            table_with_style.setStyle(TableStyle([
                ('FONT', (0, 0), (-1, -1), 'Vera'),
                ('FONTSIZE', (0, 1), (1, 0), 10),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                ('ALIGN', (0, 0), (1, 0), 'LEFT'),
            ]))
            elements.append(table_with_style)
            elements.append(PageBreak())
            reports.extend(elements)
            elements[:] = []
        else:
            elements[:] = []

        doc.build(reports)
        pdf = buffer.getvalue()
        buffer.close()
        
        return pdf


    def generate_report_child(self, sortId):
        buffer = self.buffer

        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=15)
        pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
        pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
        pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
        pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

        table_data = []
        elements = []
        reports = []

        table_data[:] = []
        order = 1
        '''
        elif sortId == 2:
            table_data.append(["Redni\nbroj", "Ime i prezime", "Zvanje"])
            districts = District.objects.all().order_by('name')
            employees = Employee.objects.all().order_by('address__district__name')
            for employee in employees:
               table_data.append([str(order) + ".", str(employee), employee.address.district.name])
               order += 1
        '''
       
        if len(table_data) > 1:
            table_with_style = Table(table_data, [0.5 * inch, 1.8 * inch, 2.5 * inch, 2 * inch])
            table_with_style.setStyle(TableStyle([
                ('FONT', (0, 0), (-1, -1), 'Vera'),
                ('FONTSIZE', (0, 1), (1, 0), 10),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                ('ALIGN', (0, 0), (1, 0), 'LEFT'),
            ]))
            elements.append(table_with_style)
            elements.append(PageBreak())
            reports.extend(elements)
            elements[:] = []
        else:
             elements[:] = []

        doc.build(reports)
        pdf = buffer.getvalue()
        buffer.close()
        return pdf
