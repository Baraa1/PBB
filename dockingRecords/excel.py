# Django
#from email import header
from django.http import HttpResponse
# Python3
from datetime import datetime
import pytz
import io
# xlxswriter
import xlsxwriter
# Custom
#from .models import DockingRecord
#from accounts.models import CustomUser
tz = pytz.timezone('Asia/Riyadh')

def cells(workbook, worksheet, records):

    header_format = workbook.add_format(
        {
            'bold': True,
            'font_size':14,
            'font_color':'#FFFFFF',
            'align':'center',
            'valign':'vcenter',
            'bg_color': '#16365C',
            'border': 5,
        }
    )
    rows_format = workbook.add_format({'font_size':14, 'align':'center', 'valign':'vcenter', 'border': 2})
    even_rows_format = workbook.add_format({'font_size':14, 'align':'center', 'valign':'vcenter', 'border': 2, 'bg_color': '#C5D9F1'})

    worksheet.set_row(0,60)
    worksheet.set_row(1,40)
    worksheet.freeze_panes(1, 0)  # Freeze the first row.

    
    worksheet.write('A1', 'Arrival Operator', header_format)
    worksheet.set_column(1, 1, 30)
    worksheet.write('B1', 'Stand', header_format)
    worksheet.set_column(2, 2, 20)
    worksheet.write('C1', 'Arrival Flight Number', header_format)
    worksheet.set_column(3, 3, 5)
    worksheet.write('D1', 'Aircraft Type', header_format)
    worksheet.write('E1', 'Aircraft Registration', header_format)
    worksheet.write('F1', 'Chocks On', header_format)
    worksheet.set_column(4, 6, 15)
    worksheet.write('G1', 'PPB_A_Docked', header_format)
    worksheet.write('H1', 'PPB_B_Docked', header_format)
    worksheet.set_column(7, 8, 15)
    worksheet.write('I1', 'Departure Operator', header_format)
    worksheet.write('J1', 'Departure Flight Number', header_format)
    worksheet.write('K1', 'PBB_A_Door Close', header_format)
    worksheet.write('L1', 'PBB_B_Door Close', header_format)
    worksheet.write('M1', 'PBB_A_Undocked', header_format)
    worksheet.write('N1', 'PBB_B_Undocked', header_format)
    worksheet.set_column(9, 14, 15)
    worksheet.write('O1', 'Remarks', header_format)
    worksheet.set_column(15, 15, 50)

    i = 2
    for record in records:
        if i%2==0:
            row_format = rows_format
        else:
            row_format = even_rows_format
        worksheet.set_row(i,40)
        worksheet.write(f'A{i}', f'{record.operator1}', row_format)
        worksheet.write(f'B{i}', f'{record.stand}', row_format)
        worksheet.write(f'C{i}', f'{record.flight_no1}', row_format)
        worksheet.write(f'D{i}', f'{record.ac_type}', row_format)
        worksheet.write(f'E{i}', f'{record.ac_reg}', row_format)
        worksheet.write(f'F{i}', f'{record.chocks_on}', row_format)
        try:
            docked = datetime.astimezone(record.docked,tz=tz)
            worksheet.write(f'G{i}', f'{docked}', row_format)
        except:
            worksheet.write(f'G{i}', f'{record.docked}', row_format)
        worksheet.write(f'H{i}', f'{record.b_docked}', row_format)
        worksheet.write(f'I{i}', f'{record.operator2}', row_format)
        worksheet.write(f'J{i}', f'{record.flight_no2}', row_format)
        worksheet.write(f'K{i}', f'{record.door_close}', row_format)
        worksheet.write(f'L{i}', f'{record.b_door_close}', row_format)
        try:
            undocked = datetime.astimezone(record.undocked,tz=tz)
            worksheet.write(f'M{i}', f'{undocked}', row_format)
        except:
            worksheet.write(f'M{i}', f'{record.undocked}', row_format)
        worksheet.write(f'N{i}', f'{record.b_undocked}', row_format)
        worksheet.write(f'O{i}', f'{record.remarks}', row_format)
        i+=1

def by_record_filter(records):
    # Create an in-memory output file for the new workbook.
    output = io.BytesIO()
    
    workbook       = xlsxwriter.Workbook(output, {'remove_timezone': True})
    worksheet      = workbook.add_worksheet()
    
    # Populate the worksheet
    cells(workbook, worksheet, records.qs)
    
    workbook.close()
    # Rewind the buffer.
    output.seek(0)

    # Set up the Http response.
    filename = f'{datetime.now().ctime()}.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response