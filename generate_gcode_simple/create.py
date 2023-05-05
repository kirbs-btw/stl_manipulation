
def main():

    content = []
    


    with open('H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/top_gcode.txt') as f:
        top = f.readlines()

    with open('H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/end_gcode.txt') as f:
        end = f.readlines()

    file = open('H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/gcode.gcode', 'w+')

    for char in top:
        file.write(char)

    for char in content:
        file.write(char)

    for char in end:
        file.write(char)


if __name__ == '__main__':
    main()