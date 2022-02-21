from PIL import Image, ImageDraw, ImageFont
import csv

def main():
    student_list = []
    with open("student_info.csv", newline="") as f:
        rows = csv.reader(f,delimiter=",")
        for index, row in enumerate(rows):
            student_list.append([row[0],row[1]])


    a4im_head = Image.new('RGB',
                        (2480, 3508),   # A4 at 300dpi
                        (255, 255, 255))  # White

    name_tag_list = []


    for student in student_list:

        student_team = convert_team_name(int(student[0]))
        student_name = student[1]

        a4im = Image.new('RGB',
                        (2480, 3508),   # A4 at 300dpi
                        (255, 255, 255))  # White
        a4im_draw = ImageDraw.Draw(a4im)
        # -------------------------------- Write team -------------------------------- #
        fnt_team = ImageFont.truetype('./MSJH.TTC', 150)
        team_w, team_h = a4im_draw.textsize(student_team, font=fnt_team)
        team_location = ((2480-team_w)/2,(1050-team_h)/2-200)
        a4im_draw.text(team_location, student_team, font=fnt_team, fill=(0, 0, 0))

        # -------------------------------- Write name -------------------------------- #
        fnt_name = ImageFont.truetype('./MSJH.TTC', 300)
        name_w, name_h = a4im_draw.textsize(student_name, font=fnt_name)
        name_location = ((2480-name_w)/2,(1050-name_h)/2+150)
        a4im_draw.text(name_location, student_name, font=fnt_name, fill=(0, 0, 0))

        # --------------------------------- Draw line -------------------------------- #
        for i in range(1,4):
            shape = [(0,1050*i),(2480,1050*i)]
            a4im_draw.line(shape,fill = "black", width = 3)
        
        name_tag_list.append(a4im)

    a4im_head.save('test.pdf', 'PDF', resolution=300, save_all = True, append_images = name_tag_list)

def convert_team_name(team):
    if(team == 1):
        return "第一組"
    elif(team == 2):
        return "第二組"
    elif(team == 3):
        return "第三組"
    elif(team == 4):
        return "第四組"
    elif(team == 5):
        return "第五組"
    elif(team == 6):
        return "第六組"

if __name__ == '__main__':
    main()
