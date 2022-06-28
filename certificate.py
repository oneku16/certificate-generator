import os
from PIL import Image, ImageDraw, ImageFont
from time import strftime as st, gmtime as gt
  

class Certificate:

    def __init__(self, student_name: str, certificate_id: str, organization_name, result: float):

        self.name=student_name# = student_name
        self.id=certificate_id # = student_id
        self.organization=organization_name # = organization_name
        self.result = result # = result
        self.dir_path=os.path.dirname(os.path.realpath(__file__))
        self.font_path="c:\Windows\Fonts\Bahnschrift.ttf"

    
    def template(self, certificate_path = None) -> str:
        
        if certificate_path is None: 
            certificate_path=os.path.join(self.dir_path,"templates\certificate.jpg")
        return certificate_path


    def draw_text(self, font=None, text_color="#000000"):

        with Image.open(self.template()) as img:
            draw = ImageDraw.Draw(img)

        if font is None:
            font=ImageFont.truetype(self.font_path, 65)

        image_width=img.width
        image_height=img.height

        def draw_(text:str, x_pos: float, y_pos:float, size:int, status = True):
        
            text_width, _=draw.textsize(text=text, font=font)
            if status:
                draw.text( xy = ((x_pos - text_width) / 2, y_pos), text=text, font=ImageFont.truetype(self.font_path, size), fill="#000000")
            else: 
                draw.text( xy = (x_pos, y_pos), text=text, font=ImageFont.truetype(self.font_path, size), fill="#000000")
        
        draw_(self.name, image_width, 525, 65)
        draw_(self.organization, image_width, 250, 85)
        draw_(st("%d.%m.%Y", gt()), 1440, 1070, 30, status = False)
        draw_(f"{self.id}", 15, 1070, 30, status = False)
        draw_(f"{'Результат'}\n{self.result}%", 1440, 175, 30, status = False)

        
        im_to_pdf = img.convert('RGB')
        im_to_pdf.save(f"certificates/{self.name}.pdf")
            
    def setId(self, student_id):
        self.id = student_id

    def getId(self):
        return self.id

    def setName(self, student_name):
        self.name = student_name

    def getName(self):
        return self.name

    def setOrganization(self, organization_name): 
        self.organization = organization_name

    def getOrganization(self):
        return self.organization

    def setResult(self, result):
        self.result = result

    def getResult(self):
        return self.result

    def getDate(self):
        return st("%d.%M.%Y", gt())

    def getAll(self):return {
        'name':f"{self.name}", 
        'certificate_id': f"{self.id}", 
        'organization':f"{self.organization}", 
        'result':f"{self.result}", 
        'date':f"{self.getDate()}"
        }

