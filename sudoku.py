# Author：Chang.

class SudokuError(Exception):
    def __init__(self, message):
        self.message = message


class Sudoku():
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as f:
            self.matrix=[]
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue
                row=[]
                for char in line:
                    if '0'<=char<='9':
                        row.append(int(char))
                if len(row)!=9:
                    raise  SudokuError('Incorrect input')
                self.matrix.append(row)
            if len(self.matrix) !=9:
                raise SudokuError('Incorrect input')
        self.matrix_=[]
        for i in range (0,9):
            column = []
            for line in self.matrix:
                column.append(line[i])
            self.matrix_.append(column)

        self.box=[]
        x=0
        y=0
        while True:
            small_box = []
            for i in range (x,x+3):
                for j in range (y,y+3):
                    small_box.append(self.matrix[i][j])
            self.box.append(small_box)

            if y+3<9:
                y+=3
            else:
                if x+3<9:
                    x+=3
                    y=0
                else:
                    break

        self.box_dict = {}
        for i in range(0,9):
            for j in range(0,45):
                if j!=4 and j != 9 and j !=14 and j!=19 and  j!=24 and j!= 29 and j!= 34 and j !=39 and j !=44:
                    self.box_dict[i,j]=''
                else:
                    if self.matrix[i][j//5]==0:
                        self.box_dict[i, j] = ''
                    else:
                        self.box_dict[i,j]=str(self.matrix[i][j//5])

        self.a='\documentclass[10pt]{article}\n' \
          '\\usepackage[left=0pt,right=0pt]{geometry}\n' \
          '\\usepackage{tikz}\n' \
          '\\usetikzlibrary{positioning}\n' \
          '\\usepackage{cancel}\n' \
          '\pagestyle{empty}\n' \
          '\n' \
          '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n' \
          '                               label=above right:{\\tiny #2},\n' \
          '                               label=below left:{\\tiny #3},\n' \
          '                               label=below right:{\\tiny #4}]{#5};}}\n' \
          '\n' \
          '\\begin{document}\n' \
          '\n' \
          '\\tikzset{every node/.style={minimum size=.5cm}}\n' \
          '\n' \
          '\\begin{center}\n' \
          '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline\n' \

        self.c='\\end{tabular}\n' \
          '\\end{center}\n' \
          '\n' \
          '\\end{document}\n'
    def preassess(self):
        for line in self.matrix:
            for element in line:
                if element==0:
                    pass
                else:
                    if line.count(element)>1:
                        return print('There is clearly no solution.')
        for line in self.matrix_:
            for element in line:
                if element==0:
                    pass
                else:
                    if line.count(element)>1:
                        return print('There is clearly no solution.')
        for line in self.box:
            for element in line:
                if element == 0:
                    pass
                else:
                    if line.count(element) > 1:
                        return print('There is clearly no solution.')
        return print('There might be a solution.')

    def bare_tex_output(self):

        box_1 = '% Line 1\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[0, 0], self.box_dict[0, 1], self.box_dict[0, 2], self.box_dict[0, 3],
                    self.box_dict[0, 4], self.box_dict[0, 5], self.box_dict[0, 6], self.box_dict[0, 7],
                    self.box_dict[0, 8], self.box_dict[0, 9], self.box_dict[0, 10], self.box_dict[0, 11],
                    self.box_dict[0, 12], self.box_dict[0, 13], self.box_dict[0, 14],
                    self.box_dict[0, 15], self.box_dict[0, 16], self.box_dict[0, 17], self.box_dict[0, 18],
                    self.box_dict[0, 19], self.box_dict[0, 20], self.box_dict[0, 21], self.box_dict[0, 22],
                    self.box_dict[0, 23], self.box_dict[0, 24], self.box_dict[0, 25], self.box_dict[0, 26],
                    self.box_dict[0, 27], self.box_dict[0, 28], self.box_dict[0, 29],
                    self.box_dict[0, 30], self.box_dict[0, 31], self.box_dict[0, 32], self.box_dict[0, 33],
                    self.box_dict[0, 34], self.box_dict[0, 35], self.box_dict[0, 36], self.box_dict[0, 37],
                    self.box_dict[0, 38], self.box_dict[0, 39], self.box_dict[0, 40], self.box_dict[0, 41],
                    self.box_dict[0, 42], self.box_dict[0, 43], self.box_dict[0, 44])
        box_2 = '% Line 2\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[1, 0], self.box_dict[1, 1], self.box_dict[1, 2], self.box_dict[1, 3],
                    self.box_dict[1, 4], self.box_dict[1, 5], self.box_dict[1, 6], self.box_dict[1, 7],
                    self.box_dict[1, 8], self.box_dict[1, 9], self.box_dict[1, 10], self.box_dict[1, 11],
                    self.box_dict[1, 12], self.box_dict[1, 13], self.box_dict[1, 14],
                    self.box_dict[1, 15], self.box_dict[1, 16], self.box_dict[1, 17], self.box_dict[1, 18],
                    self.box_dict[1, 19], self.box_dict[1, 20], self.box_dict[1, 21], self.box_dict[1, 22],
                    self.box_dict[1, 23], self.box_dict[1, 24], self.box_dict[1, 25], self.box_dict[1, 26],
                    self.box_dict[1, 27], self.box_dict[1, 28], self.box_dict[1, 29],
                    self.box_dict[1, 30], self.box_dict[1, 31], self.box_dict[1, 32], self.box_dict[1, 33],
                    self.box_dict[1, 34], self.box_dict[1, 35], self.box_dict[1, 36], self.box_dict[1, 37],
                    self.box_dict[1, 38], self.box_dict[1, 39], self.box_dict[1, 40], self.box_dict[1, 41],
                    self.box_dict[1, 42], self.box_dict[1, 43], self.box_dict[1, 44])
        box_3 = '% Line 3\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\\hline\n\n' \
            .format(self.box_dict[2, 0], self.box_dict[2, 1], self.box_dict[2, 2], self.box_dict[2, 3],
                    self.box_dict[2, 4], self.box_dict[2, 5], self.box_dict[2, 6], self.box_dict[2, 7],
                    self.box_dict[2, 8], self.box_dict[2, 9], self.box_dict[2, 10], self.box_dict[2, 11],
                    self.box_dict[2, 12], self.box_dict[2, 13], self.box_dict[2, 14],
                    self.box_dict[2, 15], self.box_dict[2, 16], self.box_dict[2, 17], self.box_dict[2, 18],
                    self.box_dict[2, 19], self.box_dict[2, 20], self.box_dict[2, 21], self.box_dict[2, 22],
                    self.box_dict[2, 23], self.box_dict[2, 24], self.box_dict[2, 25], self.box_dict[2, 26],
                    self.box_dict[2, 27], self.box_dict[2, 28], self.box_dict[2, 29],
                    self.box_dict[2, 30], self.box_dict[2, 31], self.box_dict[2, 32], self.box_dict[2, 33],
                    self.box_dict[2, 34], self.box_dict[2, 35], self.box_dict[2, 36], self.box_dict[2, 37],
                    self.box_dict[2, 38], self.box_dict[2, 39], self.box_dict[2, 40], self.box_dict[2, 41],
                    self.box_dict[2, 42], self.box_dict[2, 43], self.box_dict[2, 44])
        box_4 = '% Line 4\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[3, 0], self.box_dict[3, 1], self.box_dict[3, 2], self.box_dict[3, 3],
                    self.box_dict[3, 4], self.box_dict[3, 5], self.box_dict[3, 6], self.box_dict[3, 7],
                    self.box_dict[3, 8], self.box_dict[3, 9], self.box_dict[3, 10], self.box_dict[3, 11],
                    self.box_dict[3, 12], self.box_dict[3, 13], self.box_dict[3, 14],
                    self.box_dict[3, 15], self.box_dict[3, 16], self.box_dict[3, 17], self.box_dict[3, 18],
                    self.box_dict[3, 19], self.box_dict[3, 20], self.box_dict[3, 21], self.box_dict[3, 22],
                    self.box_dict[3, 23], self.box_dict[3, 24], self.box_dict[3, 25], self.box_dict[3, 26],
                    self.box_dict[3, 27], self.box_dict[3, 28], self.box_dict[3, 29],
                    self.box_dict[3, 30], self.box_dict[3, 31], self.box_dict[3, 32], self.box_dict[3, 33],
                    self.box_dict[3, 34], self.box_dict[3, 35], self.box_dict[3, 36], self.box_dict[3, 37],
                    self.box_dict[3, 38], self.box_dict[3, 39], self.box_dict[3, 40], self.box_dict[3, 41],
                    self.box_dict[3, 42], self.box_dict[3, 43], self.box_dict[3, 44])
        box_5 = '% Line 5\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[4, 0], self.box_dict[4, 1], self.box_dict[4, 2], self.box_dict[4, 3],
                    self.box_dict[4, 4], self.box_dict[4, 5], self.box_dict[4, 6], self.box_dict[4, 7],
                    self.box_dict[4, 8], self.box_dict[4, 9], self.box_dict[4, 10], self.box_dict[4, 11],
                    self.box_dict[4, 12], self.box_dict[4, 13], self.box_dict[4, 14],
                    self.box_dict[4, 15], self.box_dict[4, 16], self.box_dict[4, 17], self.box_dict[4, 18],
                    self.box_dict[4, 19], self.box_dict[4, 20], self.box_dict[4, 21], self.box_dict[4, 22],
                    self.box_dict[4, 23], self.box_dict[4, 24], self.box_dict[4, 25], self.box_dict[4, 26],
                    self.box_dict[4, 27], self.box_dict[4, 28], self.box_dict[4, 29],
                    self.box_dict[4, 30], self.box_dict[4, 31], self.box_dict[4, 32], self.box_dict[4, 33],
                    self.box_dict[4, 34], self.box_dict[4, 35], self.box_dict[4, 36], self.box_dict[4, 37],
                    self.box_dict[4, 38], self.box_dict[4, 39], self.box_dict[4, 40], self.box_dict[4, 41],
                    self.box_dict[4, 42], self.box_dict[4, 43], self.box_dict[4, 44])
        box_6 = '% Line 6\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\\hline\n\n' \
            .format(self.box_dict[5, 0], self.box_dict[5, 1], self.box_dict[5, 2], self.box_dict[5, 3],
                    self.box_dict[5, 4], self.box_dict[5, 5], self.box_dict[5, 6], self.box_dict[5, 7],
                    self.box_dict[5, 8], self.box_dict[5, 9], self.box_dict[5, 10], self.box_dict[5, 11],
                    self.box_dict[5, 12], self.box_dict[5, 13], self.box_dict[5, 14],
                    self.box_dict[5, 15], self.box_dict[5, 16], self.box_dict[5, 17], self.box_dict[5, 18],
                    self.box_dict[5, 19], self.box_dict[5, 20], self.box_dict[5, 21], self.box_dict[5, 22],
                    self.box_dict[5, 23], self.box_dict[5, 24], self.box_dict[5, 25], self.box_dict[5, 26],
                    self.box_dict[5, 27], self.box_dict[5, 28], self.box_dict[5, 29],
                    self.box_dict[5, 30], self.box_dict[5, 31], self.box_dict[5, 32], self.box_dict[5, 33],
                    self.box_dict[5, 34], self.box_dict[5, 35], self.box_dict[5, 36], self.box_dict[5, 37],
                    self.box_dict[5, 38], self.box_dict[5, 39], self.box_dict[5, 40], self.box_dict[5, 41],
                    self.box_dict[5, 42], self.box_dict[5, 43], self.box_dict[5, 44])
        box_7 = '% Line 7\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[6, 0], self.box_dict[6, 1], self.box_dict[6, 2], self.box_dict[6, 3],
                    self.box_dict[6, 4], self.box_dict[6, 5], self.box_dict[6, 6], self.box_dict[6, 7],
                    self.box_dict[6, 8], self.box_dict[6, 9], self.box_dict[6, 10], self.box_dict[6, 11],
                    self.box_dict[6, 12], self.box_dict[6, 13], self.box_dict[6, 14],
                    self.box_dict[6, 15], self.box_dict[6, 16], self.box_dict[6, 17], self.box_dict[6, 18],
                    self.box_dict[6, 19], self.box_dict[6, 20], self.box_dict[6, 21], self.box_dict[6, 22],
                    self.box_dict[6, 23], self.box_dict[6, 24], self.box_dict[6, 25], self.box_dict[6, 26],
                    self.box_dict[6, 27], self.box_dict[6, 28], self.box_dict[6, 29],
                    self.box_dict[6, 30], self.box_dict[6, 31], self.box_dict[6, 32], self.box_dict[6, 33],
                    self.box_dict[6, 34], self.box_dict[6, 35], self.box_dict[6, 36], self.box_dict[6, 37],
                    self.box_dict[6, 38], self.box_dict[6, 39], self.box_dict[6, 40], self.box_dict[6, 41],
                    self.box_dict[6, 42], self.box_dict[6, 43], self.box_dict[6, 44])
        box_8 = '% Line 8\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[7, 0], self.box_dict[7, 1], self.box_dict[7, 2], self.box_dict[7, 3],
                    self.box_dict[7, 4], self.box_dict[7, 5], self.box_dict[7, 6], self.box_dict[7, 7],
                    self.box_dict[7, 8], self.box_dict[7, 9], self.box_dict[7, 10], self.box_dict[7, 11],
                    self.box_dict[7, 12], self.box_dict[7, 13], self.box_dict[7, 14],
                    self.box_dict[7, 15], self.box_dict[7, 16], self.box_dict[7, 17], self.box_dict[7, 18],
                    self.box_dict[7, 19], self.box_dict[7, 20], self.box_dict[7, 21], self.box_dict[7, 22],
                    self.box_dict[7, 23], self.box_dict[7, 24], self.box_dict[7, 25], self.box_dict[7, 26],
                    self.box_dict[7, 27], self.box_dict[7, 28], self.box_dict[7, 29],
                    self.box_dict[7, 30], self.box_dict[7, 31], self.box_dict[7, 32], self.box_dict[7, 33],
                    self.box_dict[7, 34], self.box_dict[7, 35], self.box_dict[7, 36], self.box_dict[7, 37],
                    self.box_dict[7, 38], self.box_dict[7, 39], self.box_dict[7, 40], self.box_dict[7, 41],
                    self.box_dict[7, 42], self.box_dict[7, 43], self.box_dict[7, 44])
        box_9 = '% Line 9\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\\hline\n' \
            .format(self.box_dict[8, 0], self.box_dict[8, 1], self.box_dict[8, 2], self.box_dict[8, 3],
                    self.box_dict[8, 4], self.box_dict[8, 5], self.box_dict[8, 6], self.box_dict[8, 7],
                    self.box_dict[8, 8], self.box_dict[8, 9], self.box_dict[8, 10], self.box_dict[8, 11],
                    self.box_dict[8, 12], self.box_dict[8, 13], self.box_dict[8, 14],
                    self.box_dict[8, 15], self.box_dict[8, 16], self.box_dict[8, 17], self.box_dict[8, 18],
                    self.box_dict[8, 19], self.box_dict[8, 20], self.box_dict[8, 21], self.box_dict[8, 22],
                    self.box_dict[8, 23], self.box_dict[8, 24], self.box_dict[8, 25], self.box_dict[8, 26],
                    self.box_dict[8, 27], self.box_dict[8, 28], self.box_dict[8, 29],
                    self.box_dict[8, 30], self.box_dict[8, 31], self.box_dict[8, 32], self.box_dict[8, 33],
                    self.box_dict[8, 34], self.box_dict[8, 35], self.box_dict[8, 36], self.box_dict[8, 37],
                    self.box_dict[8, 38], self.box_dict[8, 39], self.box_dict[8, 40], self.box_dict[8, 41],
                    self.box_dict[8, 42], self.box_dict[8, 43], self.box_dict[8, 44])

        tex_filename = self.filename[:-4]+'_bare.tex'
        with open(tex_filename,'w') as file:
            file.writelines(self.a+box_1+box_2+box_3+box_4+box_5+box_6+box_7+box_8+box_9+self.c)


    def forced_tex_output(self):
        update = True
        L_element=[]
        for line in self.matrix:
            for element in line:
                if element != 0:
                    L_element.append(element)

        L_set_element = [1,2,3,4,5,6,7,8,9]
        L_count_element=[]
        for element in  L_set_element:
            L_count_element.append((element,L_element.count(element)))

        L_count_element.sort(key=lambda x:x[1],reverse=True)


        while update == True:


            update=False
            for i in L_count_element:

                if i[0] not in self.box[0]:
                    L_may_be_can_add = []
                    for m in range(0, 3):
                        for n in range(0, 3):
                            if self.matrix[m][n] == 0:
                                if i[0] not in self.matrix[m] and i[0] not in self.matrix_[n]:
                                    L_may_be_can_add.append((m, n))
                    if len(L_may_be_can_add) == 1:
                        self.matrix[L_may_be_can_add[0][0]][L_may_be_can_add[0][1]] = i[0]
                        self.matrix_[L_may_be_can_add[0][1]][L_may_be_can_add[0][0]] = i[0]
                        if m==0:
                            self.box[0][n]=i[0]
                        elif m==1:
                            self.box[0][n+3]
                        else:
                            self.box[0][n+6]
                        update = True

                if i[0] not in self.box[1]:
                    L_may_be_can_add = []
                    for m in range(0, 3):
                        for n in range(3, 6):
                            if self.matrix[m][n] == 0:
                                if i[0] not in self.matrix[m] and i[0] not in self.matrix_[n]:
                                    L_may_be_can_add.append((m, n))
                    if len(L_may_be_can_add) == 1:
                        self.matrix[L_may_be_can_add[0][0]][L_may_be_can_add[0][1]] = i[0]
                        self.matrix_[L_may_be_can_add[0][1]][L_may_be_can_add[0][0]] = i[0]
                        if m==0:
                            self.box[1][n-3]=i[0]
                        elif m==1:
                            self.box[1][n]
                        else:
                            self.box[1][n+3]
                        update = True

                if i[0] not in self.box[2]:
                    L_may_be_can_add = []
                    for m in range(0, 3):
                        for n in range(6, 9):
                            if self.matrix[m][n] == 0:
                                if i[0] not in self.matrix[m] and i[0] not in self.matrix_[n]:
                                    L_may_be_can_add.append((m, n))
                    if len(L_may_be_can_add) == 1:
                        self.matrix[L_may_be_can_add[0][0]][L_may_be_can_add[0][1]] = i[0]
                        self.matrix_[L_may_be_can_add[0][1]][L_may_be_can_add[0][0]] = i[0]
                        if m==0:
                            self.box[2][n-6]=i[0]
                        elif m==1:
                            self.box[2][n-3]
                        else:
                            self.box[2][n]
                        update = True

                if i[0] not in self.box[3]:
                    L_may_be_can_add = []
                    for m in range(3, 6):
                        for n in range(0, 3):
                            if self.matrix[m][n] == 0:
                                if i[0] not in self.matrix[m] and i[0] not in self.matrix_[n]:
                                    L_may_be_can_add.append((m, n))
                    if len(L_may_be_can_add) == 1:
                        self.matrix[L_may_be_can_add[0][0]][L_may_be_can_add[0][1]] = i[0]
                        self.matrix_[L_may_be_can_add[0][1]][L_may_be_can_add[0][0]] = i[0]
                        if m==3:
                            self.box[3][n]=i[0]
                        elif m==4:
                            self.box[3][n+3]
                        else:
                            self.box[3][n+6]
                        update = True

                if i[0] not in self.box[4]:
                    L_may_be_can_add = []
                    for m in range(3, 6):
                        for n in range(3, 6):
                            if self.matrix[m][n] == 0:
                                if i[0] not in self.matrix[m] and i[0] not in self.matrix_[n]:
                                    L_may_be_can_add.append((m, n))
                    if len(L_may_be_can_add) == 1:
                        self.matrix[L_may_be_can_add[0][0]][L_may_be_can_add[0][1]] = i[0]
                        self.matrix_[L_may_be_can_add[0][1]][L_may_be_can_add[0][0]] = i[0]
                        if m==3:
                            self.box[4][n-3]=i[0]
                        elif m==4:
                            self.box[4][n]
                        else:
                            self.box[4][n+3]
                        update = True

                if i[0] not in self.box[5]:
                    L_may_be_can_add = []
                    for m in range(3, 6):
                        for n in range(6, 9):
                            if self.matrix[m][n] == 0:
                                if i[0] not in self.matrix[m] and i[0] not in self.matrix_[n]:
                                    L_may_be_can_add.append((m, n))
                    if len(L_may_be_can_add) == 1:
                        self.matrix[L_may_be_can_add[0][0]][L_may_be_can_add[0][1]] = i[0]
                        self.matrix_[L_may_be_can_add[0][1]][L_may_be_can_add[0][0]] = i[0]
                        if m==3:
                            self.box[5][n-6]=i[0]
                        elif m==4:
                            self.box[5][n-3]
                        else:
                            self.box[5][n]
                        update = True

                if i[0] not in self.box[6]:
                    L_may_be_can_add = []
                    for m in range(6, 9):
                        for n in range(0, 3):
                            if self.matrix[m][n] == 0:
                                if i[0] not in self.matrix[m] and i[0] not in self.matrix_[n]:
                                    L_may_be_can_add.append((m, n))
                    if len(L_may_be_can_add) == 1:
                        self.matrix[L_may_be_can_add[0][0]][L_may_be_can_add[0][1]] = i[0]
                        self.matrix_[L_may_be_can_add[0][1]][L_may_be_can_add[0][0]] = i[0]
                        if m==6:
                            self.box[6][n]=i[0]
                        elif m==7:
                            self.box[6][n+3]
                        else:
                            self.box[6][n+6]
                        update = True

                if i[0] not in self.box[7]:
                    L_may_be_can_add = []
                    for m in range(6, 9):
                        for n in range(3, 6):
                            if self.matrix[m][n] == 0:
                                if i[0] not in self.matrix[m] and i[0] not in self.matrix_[n]:
                                    L_may_be_can_add.append((m, n))
                    if len(L_may_be_can_add) == 1:
                        self.matrix[L_may_be_can_add[0][0]][L_may_be_can_add[0][1]] = i[0]
                        self.matrix_[L_may_be_can_add[0][1]][L_may_be_can_add[0][0]] = i[0]
                        if m==6:
                            self.box[7][n-3]=i[0]
                        elif m==7:
                            self.box[7][n]
                        else:
                            self.box[7][n+3]
                        update = True

                if i[0] not in self.box[8]:

                    L_may_be_can_add = []
                    for m in range(6, 9):
                        for n in range(6, 9):
                            if self.matrix[m][n] == 0:
                                if i[0] not in self.matrix[m] and i[0] not in self.matrix_[n]:
                                    L_may_be_can_add.append((m, n))
                    if len(L_may_be_can_add) == 1:
                        self.matrix[L_may_be_can_add[0][0]][L_may_be_can_add[0][1]] = i[0]
                        self.matrix_[L_may_be_can_add[0][1]][L_may_be_can_add[0][0]] = i[0]
                        if m==6:
                            self.box[8][n-6]=i[0]
                        elif m==7:
                            self.box[8][n-3]
                        else:
                            self.box[8][n]
                        update = True



        for i in range(0,9):
            for j in range(0,45):
                if j!=4 and j != 9 and j !=14 and j!=19 and  j!=24 and j!= 29 and j!= 34 and j !=39 and j !=44:
                    self.box_dict[i,j]=''
                else:
                    if self.matrix[i][j//5]==0:
                        self.box_dict[i, j] = ''
                    else:
                        self.box_dict[i,j]=str(self.matrix[i][j//5])

        box_1 = '% Line 1\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[0, 0], self.box_dict[0, 1], self.box_dict[0, 2], self.box_dict[0, 3],
                    self.box_dict[0, 4], self.box_dict[0, 5], self.box_dict[0, 6], self.box_dict[0, 7],
                    self.box_dict[0, 8], self.box_dict[0, 9], self.box_dict[0, 10], self.box_dict[0, 11],
                    self.box_dict[0, 12], self.box_dict[0, 13], self.box_dict[0, 14],
                    self.box_dict[0, 15], self.box_dict[0, 16], self.box_dict[0, 17], self.box_dict[0, 18],
                    self.box_dict[0, 19], self.box_dict[0, 20], self.box_dict[0, 21], self.box_dict[0, 22],
                    self.box_dict[0, 23], self.box_dict[0, 24], self.box_dict[0, 25], self.box_dict[0, 26],
                    self.box_dict[0, 27], self.box_dict[0, 28], self.box_dict[0, 29],
                    self.box_dict[0, 30], self.box_dict[0, 31], self.box_dict[0, 32], self.box_dict[0, 33],
                    self.box_dict[0, 34], self.box_dict[0, 35], self.box_dict[0, 36], self.box_dict[0, 37],
                    self.box_dict[0, 38], self.box_dict[0, 39], self.box_dict[0, 40], self.box_dict[0, 41],
                    self.box_dict[0, 42], self.box_dict[0, 43], self.box_dict[0, 44])
        box_2 = '% Line 2\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[1, 0], self.box_dict[1, 1], self.box_dict[1, 2], self.box_dict[1, 3],
                    self.box_dict[1, 4], self.box_dict[1, 5], self.box_dict[1, 6], self.box_dict[1, 7],
                    self.box_dict[1, 8], self.box_dict[1, 9], self.box_dict[1, 10], self.box_dict[1, 11],
                    self.box_dict[1, 12], self.box_dict[1, 13], self.box_dict[1, 14],
                    self.box_dict[1, 15], self.box_dict[1, 16], self.box_dict[1, 17], self.box_dict[1, 18],
                    self.box_dict[1, 19], self.box_dict[1, 20], self.box_dict[1, 21], self.box_dict[1, 22],
                    self.box_dict[1, 23], self.box_dict[1, 24], self.box_dict[1, 25], self.box_dict[1, 26],
                    self.box_dict[1, 27], self.box_dict[1, 28], self.box_dict[1, 29],
                    self.box_dict[1, 30], self.box_dict[1, 31], self.box_dict[1, 32], self.box_dict[1, 33],
                    self.box_dict[1, 34], self.box_dict[1, 35], self.box_dict[1, 36], self.box_dict[1, 37],
                    self.box_dict[1, 38], self.box_dict[1, 39], self.box_dict[1, 40], self.box_dict[1, 41],
                    self.box_dict[1, 42], self.box_dict[1, 43], self.box_dict[1, 44])
        box_3 = '% Line 3\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\\hline\n\n' \
            .format(self.box_dict[2, 0], self.box_dict[2, 1], self.box_dict[2, 2], self.box_dict[2, 3],
                    self.box_dict[2, 4], self.box_dict[2, 5], self.box_dict[2, 6], self.box_dict[2, 7],
                    self.box_dict[2, 8], self.box_dict[2, 9], self.box_dict[2, 10], self.box_dict[2, 11],
                    self.box_dict[2, 12], self.box_dict[2, 13], self.box_dict[2, 14],
                    self.box_dict[2, 15], self.box_dict[2, 16], self.box_dict[2, 17], self.box_dict[2, 18],
                    self.box_dict[2, 19], self.box_dict[2, 20], self.box_dict[2, 21], self.box_dict[2, 22],
                    self.box_dict[2, 23], self.box_dict[2, 24], self.box_dict[2, 25], self.box_dict[2, 26],
                    self.box_dict[2, 27], self.box_dict[2, 28], self.box_dict[2, 29],
                    self.box_dict[2, 30], self.box_dict[2, 31], self.box_dict[2, 32], self.box_dict[2, 33],
                    self.box_dict[2, 34], self.box_dict[2, 35], self.box_dict[2, 36], self.box_dict[2, 37],
                    self.box_dict[2, 38], self.box_dict[2, 39], self.box_dict[2, 40], self.box_dict[2, 41],
                    self.box_dict[2, 42], self.box_dict[2, 43], self.box_dict[2, 44])
        box_4 = '% Line 4\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[3, 0], self.box_dict[3, 1], self.box_dict[3, 2], self.box_dict[3, 3],
                    self.box_dict[3, 4], self.box_dict[3, 5], self.box_dict[3, 6], self.box_dict[3, 7],
                    self.box_dict[3, 8], self.box_dict[3, 9], self.box_dict[3, 10], self.box_dict[3, 11],
                    self.box_dict[3, 12], self.box_dict[3, 13], self.box_dict[3, 14],
                    self.box_dict[3, 15], self.box_dict[3, 16], self.box_dict[3, 17], self.box_dict[3, 18],
                    self.box_dict[3, 19], self.box_dict[3, 20], self.box_dict[3, 21], self.box_dict[3, 22],
                    self.box_dict[3, 23], self.box_dict[3, 24], self.box_dict[3, 25], self.box_dict[3, 26],
                    self.box_dict[3, 27], self.box_dict[3, 28], self.box_dict[3, 29],
                    self.box_dict[3, 30], self.box_dict[3, 31], self.box_dict[3, 32], self.box_dict[3, 33],
                    self.box_dict[3, 34], self.box_dict[3, 35], self.box_dict[3, 36], self.box_dict[3, 37],
                    self.box_dict[3, 38], self.box_dict[3, 39], self.box_dict[3, 40], self.box_dict[3, 41],
                    self.box_dict[3, 42], self.box_dict[3, 43], self.box_dict[3, 44])
        box_5 = '% Line 5\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[4, 0], self.box_dict[4, 1], self.box_dict[4, 2], self.box_dict[4, 3],
                    self.box_dict[4, 4], self.box_dict[4, 5], self.box_dict[4, 6], self.box_dict[4, 7],
                    self.box_dict[4, 8], self.box_dict[4, 9], self.box_dict[4, 10], self.box_dict[4, 11],
                    self.box_dict[4, 12], self.box_dict[4, 13], self.box_dict[4, 14],
                    self.box_dict[4, 15], self.box_dict[4, 16], self.box_dict[4, 17], self.box_dict[4, 18],
                    self.box_dict[4, 19], self.box_dict[4, 20], self.box_dict[4, 21], self.box_dict[4, 22],
                    self.box_dict[4, 23], self.box_dict[4, 24], self.box_dict[4, 25], self.box_dict[4, 26],
                    self.box_dict[4, 27], self.box_dict[4, 28], self.box_dict[4, 29],
                    self.box_dict[4, 30], self.box_dict[4, 31], self.box_dict[4, 32], self.box_dict[4, 33],
                    self.box_dict[4, 34], self.box_dict[4, 35], self.box_dict[4, 36], self.box_dict[4, 37],
                    self.box_dict[4, 38], self.box_dict[4, 39], self.box_dict[4, 40], self.box_dict[4, 41],
                    self.box_dict[4, 42], self.box_dict[4, 43], self.box_dict[4, 44])
        box_6 = '% Line 6\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\\hline\n\n' \
            .format(self.box_dict[5, 0], self.box_dict[5, 1], self.box_dict[5, 2], self.box_dict[5, 3],
                    self.box_dict[5, 4], self.box_dict[5, 5], self.box_dict[5, 6], self.box_dict[5, 7],
                    self.box_dict[5, 8], self.box_dict[5, 9], self.box_dict[5, 10], self.box_dict[5, 11],
                    self.box_dict[5, 12], self.box_dict[5, 13], self.box_dict[5, 14],
                    self.box_dict[5, 15], self.box_dict[5, 16], self.box_dict[5, 17], self.box_dict[5, 18],
                    self.box_dict[5, 19], self.box_dict[5, 20], self.box_dict[5, 21], self.box_dict[5, 22],
                    self.box_dict[5, 23], self.box_dict[5, 24], self.box_dict[5, 25], self.box_dict[5, 26],
                    self.box_dict[5, 27], self.box_dict[5, 28], self.box_dict[5, 29],
                    self.box_dict[5, 30], self.box_dict[5, 31], self.box_dict[5, 32], self.box_dict[5, 33],
                    self.box_dict[5, 34], self.box_dict[5, 35], self.box_dict[5, 36], self.box_dict[5, 37],
                    self.box_dict[5, 38], self.box_dict[5, 39], self.box_dict[5, 40], self.box_dict[5, 41],
                    self.box_dict[5, 42], self.box_dict[5, 43], self.box_dict[5, 44])
        box_7 = '% Line 7\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[6, 0], self.box_dict[6, 1], self.box_dict[6, 2], self.box_dict[6, 3],
                    self.box_dict[6, 4], self.box_dict[6, 5], self.box_dict[6, 6], self.box_dict[6, 7],
                    self.box_dict[6, 8], self.box_dict[6, 9], self.box_dict[6, 10], self.box_dict[6, 11],
                    self.box_dict[6, 12], self.box_dict[6, 13], self.box_dict[6, 14],
                    self.box_dict[6, 15], self.box_dict[6, 16], self.box_dict[6, 17], self.box_dict[6, 18],
                    self.box_dict[6, 19], self.box_dict[6, 20], self.box_dict[6, 21], self.box_dict[6, 22],
                    self.box_dict[6, 23], self.box_dict[6, 24], self.box_dict[6, 25], self.box_dict[6, 26],
                    self.box_dict[6, 27], self.box_dict[6, 28], self.box_dict[6, 29],
                    self.box_dict[6, 30], self.box_dict[6, 31], self.box_dict[6, 32], self.box_dict[6, 33],
                    self.box_dict[6, 34], self.box_dict[6, 35], self.box_dict[6, 36], self.box_dict[6, 37],
                    self.box_dict[6, 38], self.box_dict[6, 39], self.box_dict[6, 40], self.box_dict[6, 41],
                    self.box_dict[6, 42], self.box_dict[6, 43], self.box_dict[6, 44])
        box_8 = '% Line 8\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[7, 0], self.box_dict[7, 1], self.box_dict[7, 2], self.box_dict[7, 3],
                    self.box_dict[7, 4], self.box_dict[7, 5], self.box_dict[7, 6], self.box_dict[7, 7],
                    self.box_dict[7, 8], self.box_dict[7, 9], self.box_dict[7, 10], self.box_dict[7, 11],
                    self.box_dict[7, 12], self.box_dict[7, 13], self.box_dict[7, 14],
                    self.box_dict[7, 15], self.box_dict[7, 16], self.box_dict[7, 17], self.box_dict[7, 18],
                    self.box_dict[7, 19], self.box_dict[7, 20], self.box_dict[7, 21], self.box_dict[7, 22],
                    self.box_dict[7, 23], self.box_dict[7, 24], self.box_dict[7, 25], self.box_dict[7, 26],
                    self.box_dict[7, 27], self.box_dict[7, 28], self.box_dict[7, 29],
                    self.box_dict[7, 30], self.box_dict[7, 31], self.box_dict[7, 32], self.box_dict[7, 33],
                    self.box_dict[7, 34], self.box_dict[7, 35], self.box_dict[7, 36], self.box_dict[7, 37],
                    self.box_dict[7, 38], self.box_dict[7, 39], self.box_dict[7, 40], self.box_dict[7, 41],
                    self.box_dict[7, 42], self.box_dict[7, 43], self.box_dict[7, 44])
        box_9 = '% Line 9\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
                     '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\\hline\n' \
            .format(self.box_dict[8, 0], self.box_dict[8, 1], self.box_dict[8, 2], self.box_dict[8, 3],
                    self.box_dict[8, 4], self.box_dict[8, 5], self.box_dict[8, 6], self.box_dict[8, 7],
                    self.box_dict[8, 8], self.box_dict[8, 9], self.box_dict[8, 10], self.box_dict[8, 11],
                    self.box_dict[8, 12], self.box_dict[8, 13], self.box_dict[8, 14],
                    self.box_dict[8, 15], self.box_dict[8, 16], self.box_dict[8, 17], self.box_dict[8, 18],
                    self.box_dict[8, 19], self.box_dict[8, 20], self.box_dict[8, 21], self.box_dict[8, 22],
                    self.box_dict[8, 23], self.box_dict[8, 24], self.box_dict[8, 25], self.box_dict[8, 26],
                    self.box_dict[8, 27], self.box_dict[8, 28], self.box_dict[8, 29],
                    self.box_dict[8, 30], self.box_dict[8, 31], self.box_dict[8, 32], self.box_dict[8, 33],
                    self.box_dict[8, 34], self.box_dict[8, 35], self.box_dict[8, 36], self.box_dict[8, 37],
                    self.box_dict[8, 38], self.box_dict[8, 39], self.box_dict[8, 40], self.box_dict[8, 41],
                    self.box_dict[8, 42], self.box_dict[8, 43], self.box_dict[8, 44])
        tex_filename = self.filename[:-4]+'_forced.tex'
        with open(tex_filename,'w') as file:
            file.writelines(self.a+box_1+box_2+box_3+box_4+box_5+box_6+box_7+box_8+box_9+self.c)

    def marked_tex_output(self):
        L_can_add_all_points = []
        dict_can_add={}
        for i in range (0,9):
            for j in range (0,9):
                L_can_add = [1,2,3,4,5,6,7,8,9]
                if self.matrix[i][j]==0:
                    if 0<=i<=2 and 0<=j<=2:
                        which_box = 0
                    elif 0<=i<=2 and 3<=j<=5:
                        which_box = 1
                    elif 0<=i<=2 and 6<=j<=8:
                        which_box = 2
                    elif 3<=i<=5 and 0<=j<=2:
                        which_box = 3
                    elif 3<=i<=5 and 3<=j<=5:
                        which_box = 4
                    elif 3<=i<=5 and 6<=j<=8:
                        which_box = 5
                    elif 6<=i<=8 and 0<=j<=2:
                        which_box = 6
                    elif 6<=i<=8 and 3<=j<=5:
                        which_box = 7
                    else:
                        which_box = 8
                    for x in self.box[which_box]:
                        if x!=0 and x in L_can_add:
                            L_can_add.remove(x)
                    for x in self.matrix[i]:
                        if x!=0 and x in L_can_add:
                            L_can_add.remove(x)
                    for y in self.matrix_[j]:
                        if y!=0 and y in L_can_add:
                            L_can_add.remove(y)
                    L_can_add_all_points.append(L_can_add)
                else:
                    L_can_add_all_points.append(0)

        a=0
        for i in range(0,9):
            for j in range (0,9):
                dict_can_add[i,j]=L_can_add_all_points[a]
                a+=1


        big_dict={}
        for i in range (0,9):
            for j in range (0,9):
                big_dict[i,j]=[(i,j*5),(i,j*5+1),(i,j*5+2),(i,j*5+3),(i,j*5+4)]


        for i in range(0, 9):
            for j in range(0, 9):
                if dict_can_add[i,j]!=0:
                    for element in dict_can_add[i,j]:
                        if element==1 or element==2:
                            self.box_dict[big_dict[i, j][0][0],big_dict[i, j][0][1]]+=str(element)+' '
                        if element==3 or element==4:
                            self.box_dict[big_dict[i, j][1][0], big_dict[i, j][1][1]] += str(element)+' '
                        if element==5 or element==6:
                            self.box_dict[big_dict[i, j][2][0], big_dict[i, j][2][1]] += str(element)+' '
                        if element==7 or element==8 or element==9:
                            self.box_dict[big_dict[i, j][3][0], big_dict[i, j][3][1]] += str(element)+' '

        for i in range (0,9):
            for j in range (0,45):
                if len(self.box_dict[i,j])!=1:
                    self.box_dict[i,j]=self.box_dict[i,j][:-1]


        box_1=  '% Line 1\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n'\
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[0, 0], self.box_dict[0, 1], self.box_dict[0, 2], self.box_dict[0, 3],
                    self.box_dict[0, 4], self.box_dict[0, 5], self.box_dict[0, 6], self.box_dict[0, 7],
                    self.box_dict[0, 8], self.box_dict[0, 9], self.box_dict[0, 10], self.box_dict[0, 11],
                    self.box_dict[0, 12], self.box_dict[0, 13], self.box_dict[0, 14],
                    self.box_dict[0, 15], self.box_dict[0, 16], self.box_dict[0, 17], self.box_dict[0, 18],
                    self.box_dict[0, 19], self.box_dict[0, 20], self.box_dict[0, 21], self.box_dict[0, 22],
                    self.box_dict[0, 23], self.box_dict[0, 24], self.box_dict[0, 25], self.box_dict[0, 26],
                    self.box_dict[0, 27], self.box_dict[0, 28], self.box_dict[0, 29],
                    self.box_dict[0, 30], self.box_dict[0, 31], self.box_dict[0, 32], self.box_dict[0, 33],
                    self.box_dict[0, 34], self.box_dict[0, 35], self.box_dict[0, 36], self.box_dict[0, 37],
                    self.box_dict[0, 38], self.box_dict[0, 39], self.box_dict[0, 40], self.box_dict[0, 41],
                    self.box_dict[0, 42], self.box_dict[0, 43], self.box_dict[0, 44])
        box_2=  '% Line 2\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n'\
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[1, 0], self.box_dict[1, 1], self.box_dict[1, 2], self.box_dict[1, 3],
                    self.box_dict[1, 4], self.box_dict[1, 5], self.box_dict[1, 6], self.box_dict[1, 7],
                    self.box_dict[1, 8], self.box_dict[1, 9], self.box_dict[1, 10], self.box_dict[1, 11],
                    self.box_dict[1, 12], self.box_dict[1, 13], self.box_dict[1, 14],
                    self.box_dict[1, 15], self.box_dict[1, 16], self.box_dict[1, 17], self.box_dict[1, 18],
                    self.box_dict[1, 19], self.box_dict[1, 20], self.box_dict[1, 21], self.box_dict[1, 22],
                    self.box_dict[1, 23], self.box_dict[1, 24], self.box_dict[1, 25], self.box_dict[1, 26],
                    self.box_dict[1, 27], self.box_dict[1, 28], self.box_dict[1, 29],
                    self.box_dict[1, 30], self.box_dict[1, 31], self.box_dict[1, 32], self.box_dict[1, 33],
                    self.box_dict[1, 34], self.box_dict[1, 35], self.box_dict[1, 36], self.box_dict[1, 37],
                    self.box_dict[1, 38], self.box_dict[1, 39], self.box_dict[1, 40], self.box_dict[1, 41],
                    self.box_dict[1, 42], self.box_dict[1, 43], self.box_dict[1, 44])
        box_3=  '% Line 3\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n'\
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\\hline\n\n' \
            .format(self.box_dict[2, 0], self.box_dict[2, 1], self.box_dict[2, 2], self.box_dict[2, 3],
                    self.box_dict[2, 4], self.box_dict[2, 5], self.box_dict[2, 6], self.box_dict[2, 7],
                    self.box_dict[2, 8], self.box_dict[2, 9], self.box_dict[2, 10], self.box_dict[2, 11],
                    self.box_dict[2, 12], self.box_dict[2, 13], self.box_dict[2, 14],
                    self.box_dict[2, 15], self.box_dict[2, 16], self.box_dict[2, 17], self.box_dict[2, 18],
                    self.box_dict[2, 19], self.box_dict[2, 20], self.box_dict[2, 21], self.box_dict[2, 22],
                    self.box_dict[2, 23], self.box_dict[2, 24], self.box_dict[2, 25], self.box_dict[2, 26],
                    self.box_dict[2, 27], self.box_dict[2, 28], self.box_dict[2, 29],
                    self.box_dict[2, 30], self.box_dict[2, 31], self.box_dict[2, 32], self.box_dict[2, 33],
                    self.box_dict[2, 34], self.box_dict[2, 35], self.box_dict[2, 36], self.box_dict[2, 37],
                    self.box_dict[2, 38], self.box_dict[2, 39], self.box_dict[2, 40], self.box_dict[2, 41],
                    self.box_dict[2, 42], self.box_dict[2, 43], self.box_dict[2, 44])
        box_4=  '% Line 4\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n'\
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[3, 0], self.box_dict[3, 1], self.box_dict[3, 2], self.box_dict[3, 3],
                    self.box_dict[3, 4], self.box_dict[3, 5], self.box_dict[3, 6], self.box_dict[3, 7],
                    self.box_dict[3, 8], self.box_dict[3, 9], self.box_dict[3, 10], self.box_dict[3, 11],
                    self.box_dict[3, 12], self.box_dict[3, 13], self.box_dict[3, 14],
                    self.box_dict[3, 15], self.box_dict[3, 16], self.box_dict[3, 17], self.box_dict[3, 18],
                    self.box_dict[3, 19], self.box_dict[3, 20], self.box_dict[3, 21], self.box_dict[3, 22],
                    self.box_dict[3, 23], self.box_dict[3, 24], self.box_dict[3, 25], self.box_dict[3, 26],
                    self.box_dict[3, 27], self.box_dict[3, 28], self.box_dict[3, 29],
                    self.box_dict[3, 30], self.box_dict[3, 31], self.box_dict[3, 32], self.box_dict[3, 33],
                    self.box_dict[3, 34], self.box_dict[3, 35], self.box_dict[3, 36], self.box_dict[3, 37],
                    self.box_dict[3, 38], self.box_dict[3, 39], self.box_dict[3, 40], self.box_dict[3, 41],
                    self.box_dict[3, 42], self.box_dict[3, 43], self.box_dict[3, 44])
        box_5=  '% Line 5\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n'\
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[4, 0], self.box_dict[4, 1], self.box_dict[4, 2], self.box_dict[4, 3],
                    self.box_dict[4, 4], self.box_dict[4, 5], self.box_dict[4, 6], self.box_dict[4, 7],
                    self.box_dict[4, 8], self.box_dict[4, 9], self.box_dict[4, 10], self.box_dict[4, 11],
                    self.box_dict[4, 12], self.box_dict[4, 13], self.box_dict[4, 14],
                    self.box_dict[4, 15], self.box_dict[4, 16], self.box_dict[4, 17], self.box_dict[4, 18],
                    self.box_dict[4, 19], self.box_dict[4, 20], self.box_dict[4, 21], self.box_dict[4, 22],
                    self.box_dict[4, 23], self.box_dict[4, 24], self.box_dict[4, 25], self.box_dict[4, 26],
                    self.box_dict[4, 27], self.box_dict[4, 28], self.box_dict[4, 29],
                    self.box_dict[4, 30], self.box_dict[4, 31], self.box_dict[4, 32], self.box_dict[4, 33],
                    self.box_dict[4, 34], self.box_dict[4, 35], self.box_dict[4, 36], self.box_dict[4, 37],
                    self.box_dict[4, 38], self.box_dict[4, 39], self.box_dict[4, 40], self.box_dict[4, 41],
                    self.box_dict[4, 42], self.box_dict[4, 43], self.box_dict[4, 44])
        box_6=  '% Line 6\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n'\
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\\hline\n\n' \
            .format(self.box_dict[5, 0], self.box_dict[5, 1], self.box_dict[5, 2], self.box_dict[5, 3],
                    self.box_dict[5, 4], self.box_dict[5, 5], self.box_dict[5, 6], self.box_dict[5, 7],
                    self.box_dict[5, 8], self.box_dict[5, 9], self.box_dict[5, 10], self.box_dict[5, 11],
                    self.box_dict[5, 12], self.box_dict[5, 13], self.box_dict[5, 14],
                    self.box_dict[5, 15], self.box_dict[5, 16], self.box_dict[5, 17], self.box_dict[5, 18],
                    self.box_dict[5, 19], self.box_dict[5, 20], self.box_dict[5, 21], self.box_dict[5, 22],
                    self.box_dict[5, 23], self.box_dict[5, 24], self.box_dict[5, 25], self.box_dict[5, 26],
                    self.box_dict[5, 27], self.box_dict[5, 28], self.box_dict[5, 29],
                    self.box_dict[5, 30], self.box_dict[5, 31], self.box_dict[5, 32], self.box_dict[5, 33],
                    self.box_dict[5, 34], self.box_dict[5, 35], self.box_dict[5, 36], self.box_dict[5, 37],
                    self.box_dict[5, 38], self.box_dict[5, 39], self.box_dict[5, 40], self.box_dict[5, 41],
                    self.box_dict[5, 42], self.box_dict[5, 43], self.box_dict[5, 44])
        box_7=  '% Line 7\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n'\
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[6, 0], self.box_dict[6, 1], self.box_dict[6, 2], self.box_dict[6, 3],
                    self.box_dict[6, 4], self.box_dict[6, 5], self.box_dict[6, 6], self.box_dict[6, 7],
                    self.box_dict[6, 8], self.box_dict[6, 9], self.box_dict[6, 10], self.box_dict[6, 11],
                    self.box_dict[6, 12], self.box_dict[6, 13], self.box_dict[6, 14],
                    self.box_dict[6, 15], self.box_dict[6, 16], self.box_dict[6, 17], self.box_dict[6, 18],
                    self.box_dict[6, 19], self.box_dict[6, 20], self.box_dict[6, 21], self.box_dict[6, 22],
                    self.box_dict[6, 23], self.box_dict[6, 24], self.box_dict[6, 25], self.box_dict[6, 26],
                    self.box_dict[6, 27], self.box_dict[6, 28], self.box_dict[6, 29],
                    self.box_dict[6, 30], self.box_dict[6, 31], self.box_dict[6, 32], self.box_dict[6, 33],
                    self.box_dict[6, 34], self.box_dict[6, 35], self.box_dict[6, 36], self.box_dict[6, 37],
                    self.box_dict[6, 38], self.box_dict[6, 39], self.box_dict[6, 40], self.box_dict[6, 41],
                    self.box_dict[6, 42], self.box_dict[6, 43], self.box_dict[6, 44])
        box_8=  '% Line 8\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n'\
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\n\n' \
            .format(self.box_dict[7, 0], self.box_dict[7, 1], self.box_dict[7, 2], self.box_dict[7, 3],
                    self.box_dict[7, 4], self.box_dict[7, 5], self.box_dict[7, 6], self.box_dict[7, 7],
                    self.box_dict[7, 8], self.box_dict[7, 9], self.box_dict[7, 10], self.box_dict[7, 11],
                    self.box_dict[7, 12], self.box_dict[7, 13], self.box_dict[7, 14],
                    self.box_dict[7, 15], self.box_dict[7, 16], self.box_dict[7, 17], self.box_dict[7, 18],
                    self.box_dict[7, 19], self.box_dict[7, 20], self.box_dict[7, 21], self.box_dict[7, 22],
                    self.box_dict[7, 23], self.box_dict[7, 24], self.box_dict[7, 25], self.box_dict[7, 26],
                    self.box_dict[7, 27], self.box_dict[7, 28], self.box_dict[7, 29],
                    self.box_dict[7, 30], self.box_dict[7, 31], self.box_dict[7, 32], self.box_dict[7, 33],
                    self.box_dict[7, 34], self.box_dict[7, 35], self.box_dict[7, 36], self.box_dict[7, 37],
                    self.box_dict[7, 38], self.box_dict[7, 39], self.box_dict[7, 40], self.box_dict[7, 41],
                    self.box_dict[7, 42], self.box_dict[7, 43], self.box_dict[7, 44])
        box_9=  '% Line 9\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n'\
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} &\n' \
          '\\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} & \\N{{{}}}{{{}}}{{{}}}{{{}}}{{{}}} \\\ \hline\\hline\n' \
            .format(self.box_dict[8, 0], self.box_dict[8, 1], self.box_dict[8, 2], self.box_dict[8, 3],
                    self.box_dict[8, 4], self.box_dict[8, 5], self.box_dict[8, 6], self.box_dict[8, 7],
                    self.box_dict[8, 8], self.box_dict[8, 9], self.box_dict[8, 10], self.box_dict[8, 11],
                    self.box_dict[8, 12], self.box_dict[8, 13], self.box_dict[8, 14],
                    self.box_dict[8, 15], self.box_dict[8, 16], self.box_dict[8, 17], self.box_dict[8, 18],
                    self.box_dict[8, 19], self.box_dict[8, 20], self.box_dict[8, 21], self.box_dict[8, 22],
                    self.box_dict[8, 23], self.box_dict[8, 24], self.box_dict[8, 25], self.box_dict[8, 26],
                    self.box_dict[8, 27], self.box_dict[8, 28], self.box_dict[8, 29],
                    self.box_dict[8, 30], self.box_dict[8, 31], self.box_dict[8, 32], self.box_dict[8, 33],
                    self.box_dict[8, 34], self.box_dict[8, 35], self.box_dict[8, 36], self.box_dict[8, 37],
                    self.box_dict[8, 38], self.box_dict[8, 39], self.box_dict[8, 40], self.box_dict[8, 41],
                    self.box_dict[8, 42], self.box_dict[8, 43], self.box_dict[8, 44])
        tex_filename = self.filename[:-4]+'_marked.tex'
        with open(tex_filename,'w') as file:
            file.writelines(self.a+box_1+box_2+box_3+box_4+box_5+box_6+box_7+box_8+box_9+self.c)


