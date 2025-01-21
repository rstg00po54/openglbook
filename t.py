import PyPDF2

def split_pdf(input_pdf, output_pdf, start_page, end_page):
    # 打开PDF文件
    with open(input_pdf, 'rb') as in_file:
        pdf_reader = PyPDF2.PdfReader(in_file)
        pdf_writer = PyPDF2.PdfWriter()
        
        # 选择要拆分的页面范围
        for page_num in range(start_page, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        
        # 将拆分的页面写入新的PDF文件
        with open(output_pdf, 'wb') as out_file:
            pdf_writer.write(out_file)

# 示例：拆分 PDF 文件
input_pdf = "OpenGL超级宝典  第5版_1.pdf"  # 输入文件
output_pdf = "OpenGL超级宝典  第5版 3.pdf"  # 输出文件
start_page = 413  # 起始页 (0 为第一页)
end_page = 718  # 结束页 (不包含该页)
# 0-230	0-250
# 230-392	251-412
split_pdf(input_pdf, output_pdf, start_page, end_page)
