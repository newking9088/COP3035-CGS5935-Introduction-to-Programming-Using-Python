#This program is an example of writing some of the features
#of the xlsxwriter module.

import xlsxwriter
def main():
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('demo.xlsx')
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    #worksheet.write('A1', 'Hello')   # A1 Notation
    worksheet.write(0,0, 'Hello')     # row-column Notation

    # Text with formatting.
    worksheet.write('A2', 'World', bold)

    # Write some numbers, with row/column notation.
    worksheet.write(2, 0, 123)       #A3
    worksheet.write(3, 0, 123.456)   #A4

    # Insert an image.
    #worksheet.insert_image('B5', 'logo.png')

    #Row-column notation is useful if you are referring to cells programmatically:
    for cols in range(2, 5):
        worksheet.write(1, cols , 'Hmm')

    #A1 notation is useful for setting up a worksheet manually
    #and for working with formulas:
    worksheet.write('H1', 200)
    worksheet.write('H2', '=H1+1')

    # Create a format to use in the merged range.
    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'yellow'})


    #In general when using the XlsxWriter module you can 
    #use A1 notation anywhereyou can use row-column notation. 
    #This also applies to methods that take a range of cells:
    worksheet.merge_range(2, 1, 3, 3, 'Merged Cells', merge_format)
    worksheet.merge_range('B3:D4',    'Merged Cells', merge_format)

    # Merge 3 cells.
    worksheet.merge_range('B4:D4', 'Merged Range', merge_format)

    # Merge 3 cells over two rows.
    worksheet.merge_range('B7:D8', 'Merged Range', merge_format)

    workbook.close()
main()
