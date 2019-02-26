# Author：Chang.

# !/usr/bin/env python
# -*-coding: utf-8 -*-


import numpy as np
import copy
import sys
from itertools import combinations, starmap


def read_sudoku(filepath):
    """
    :param filepath:
    :return: int list which stores the sudoku
    """
    fp = open(filepath, 'r')
    str = fp.readlines()
    fp.close()
    sudoku1 = []
    sudoku = []
    for i in str:
        L = list(i)
        for j in L:
            if '0' <= j <= '9':
                sudoku1.append(i)
                break
        else:
            pass
    sudoku1 = [i.replace(' ', '') for i in sudoku1]
    sudoku = ''

    for i in sudoku1:
        sudoku += i[:-1]
    if ',' in str:
        sudoku = str.strip().replace('\n', '').replace(' ', '').split(',')
    elif ' ' in str:
        sudoku = str.strip().split()

    for i in sudoku:
        if i == '': sudoku.remove(i)

    if valid_char(sudoku) and len(sudoku) == 81:
        return True, [int(i) for i in sudoku]
    else:
        # print(valid_char(sudoku))
        return False, []


def valid_char(sudoku):
    ret = True
    for i in sudoku:
        if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            ret = False
            break
    return ret


def tex_header():
    print(r'''\documentclass[10pt]{article}
\usepackage[left=0pt,right=0pt]{geometry}
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{cancel}
\pagestyle{empty}

\newcommand{\N}[5]{\tikz{\node[label=above left:{\tiny #1},
                               label=above right:{\tiny #2},
                               label=below left:{\tiny #3},
                               label=below right:{\tiny #4}]{#5};}}

\begin{document}

\tikzset{every node/.style={minimum size=.5cm}}

\begin{center}
\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline''')


def digit_list2string(cor, str5):
    ret = ''
    if str5 == '':
        for digit in cor:
            if isinstance(digit, float):
                ret = ret + ' ' + r'\cancel{' + str(digit).split('.')[0] + '}'
            else:
                ret = ret + ' ' + str(digit)
    else:
        for digit in cor:
            ret = ret + ' ' + r'\cancel{' + str(digit).split('.')[0] + '}'
    return ret.strip()


def tex_rows(blist, withcancel):
    for i in range(9):
        print(r'%' + ' ' + 'Line %d' % (i + 1))
        for j in range(9):
            if j == 3 or j == 6:
                print('\n', end='')

            if not isinstance(blist[i, j], list) and 0 == blist[i, j]:
                print(r'\N{}{}{}{}{}', end='')
            elif not isinstance(blist[i, j], list) and 0 != blist[i, j]:
                print(r'\N{}{}{}{}{%d}' % (blist[i][j],), end='')
            elif isinstance(blist[i, j], list):
                cor1, cor2, cor3, cor4 = ([], [], [], [])
                str1, str2, str3, str4, str5 = ('', '', '', '', '')
                cnt, cor5 = (0, 0)
                for digit in blist[i, j]:
                    if int(digit) in [1, 2]:
                        cor1.append(digit)
                    elif int(digit) in [3, 4]:
                        cor2.append(digit)
                    elif int(digit) in [5, 6]:
                        cor3.append(digit)
                    elif int(digit) in [7, 8, 9]:
                        cor4.append(digit)
                    if not isinstance(digit, float):
                        cnt += 1
                        cor5 = digit
                if cnt == 1:
                    str5 = str(cor5)
                cor1, cor2, cor3, cor4 = map(lambda x: sorted(x), [cor1, cor2, cor3, cor4])
                str1, str2, str3, str4 = starmap(digit_list2string,
                                                 [(cor1, str5), (cor2, str5), (cor3, str5), (cor4, str5)])

                print(r'\N{%s}{%s}{%s}{%s}{%s}' % (str1, str2, str3, str4, str5), end='')
            if j in (0, 1, 3, 4, 6, 7):
                print(r' & ', end='')
            elif j in (2, 5):
                print(r' &', end='')
        if i in (2, 5, 8):
            print(r' \\ \hline\hline')
        else:
            print(r' \\ \hline')
        if i != 8:
            print()


def tex_tail():
    print('''\end{tabular}
\end{center}

\end{document}''')


def write_tex(filepath, blist, withcancel):
    # tex_rows(blist)
    fp = open(filepath, 'w')
    oldstdout = sys.stdout
    sys.stdout = fp
    tex_header()
    tex_rows(blist, withcancel)
    tex_tail()
    fp.close()
    sys.stdout = oldstdout
    fp = open(filepath, 'rb')
    string = fp.read().replace(b'\r\n', b'\n').replace(b'\r', b'\n')
    f1 = open(filepath, 'wb')
    f1.write(string)
    f1.close()


def getcol(y, data):
    col = []
    for i in range(1, 10):
        col.append(data[9 * (i - 1) + y - 1])
    return col


def getrow(x, data):
    return data[9 * (x - 1):9 * (x - 1) + 9]


def getbox(x, y, data):
    if x in [1, 2, 3] and y in [1, 2, 3]:  # box1
        return data[:3] + data[9:12] + data[18:21]
    elif x in [1, 2, 3] and y in [4, 5, 6]:  # box2
        return data[3:6] + data[12:15] + data[21:24]
    elif x in [1, 2, 3] and y in [7, 8, 9]:  # box3
        return data[6:9] + data[15:18] + data[24:27]
    elif x in [4, 5, 6] and y in [1, 2, 3]:  # box4
        return data[27:30] + data[36:39] + data[45:48]
    elif x in [4, 5, 6] and y in [4, 5, 6]:  # box5
        return data[30:33] + data[39:42] + data[48:51]
    elif x in [4, 5, 6] and y in [7, 8, 9]:  # box6
        return data[33:36] + data[42:45] + data[51:54]
    elif x in [7, 8, 9] and y in [1, 2, 3]:  # box7
        return data[54:57] + data[63:66] + data[72:75]
    elif x in [7, 8, 9] and y in [4, 5, 6]:  # box8
        return data[57:60] + data[66:69] + data[75:78]
    elif x in [7, 8, 9] and y in [7, 8, 9]:  # box9
        return data[60:63] + data[69:72] + data[78:]


def get_freq_nums(data):
    dic = {}
    for i in range(1, 10): dic[i] = data.count(i)
    freq_l = []
    times = list(dic.values())
    times.sort()
    for i in times:  # find the most frequent digit
        for j in range(1, 10):
            if i == dic[j] and j not in freq_l:
                freq_l.append(j)
    freq_l.reverse()
    return freq_l


class preem():
    def __init__(self):
        self.digits = []
        self.locat = []
        self.dimension = ''


class Sudoku:
    def __init__(self, filename):
        self.value = np.array([[0] * 9] * 9, dtype=object)
        self.data = []
        self.filename = filename.split('.')[0]
        self.bare = []
        self.forced = []
        self.marked = []
        self.worked = []
        self.prplist = []
        self._init_value()
        self.valid = self._preassess(self.data)
        self._bare_tex_output()
        # self._marked_tex_output()
        self._forced_tex_output()
        self._marked_tex_output()
        self._worked_tex_output()

    def _init_value(self):
        data = read_sudoku(self.filename + '.txt')
        if data[0]:
            self.data = data[1]
        else:
            print("sudoku.SudokuError: Incorrect input")
            return
        for x in range(1, 10):
            for y in range(1, 10):
                self.value[x - 1][y - 1] = self.data[9 * (x - 1) + y - 1]

    def preassess(self):
        if len(self.data) == 0:
            return
        if self.valid:
            print("There might be a solution.")
        else:
            print("There is clearly no solution.")

    def _preassess(self, data):
        ret = True
        if len(self.data) == 0:
            return False
        # print(self.value)
        for x in range(1, 10):
            for y in range(1, 10):
                col = getcol(y, data)
                row = getrow(x, data)
                box = getbox(x, y, data)
                # print(col)
                # print()
                col = list(filter(lambda x: x != 0, col))
                row = list(filter(lambda x: x != 0, row))
                box = list(filter(lambda x: x != 0, box))
                # print(col)

                if len(row) == len(set(row)) and len(col) == len(set(col)) and len(box) == len(set(box)):
                    pass
                else:
                    # print(x,y)
                    ret = False
                    break
        return ret

    def bare_tex_output(self):
        if len(self.data) == 0:
            return
        write_tex(self.filename + '_bare.tex', self.bare, 0)

    def _bare_tex_output(self):
        if len(self.data) == 0:
            return
        else:
            self.bare = np.array(self.data).reshape(9, -1)

    def forced_tex_output(self):
        if len(self.data) == 0 or not self.valid:
            return
        write_tex(self.filename + '_forced.tex', self.forced, 0)

    def _forced_tex_output(self):
        # print(self.value)
        if len(self.data) == 0 or not self.valid:
            return
        while self._fill_in_forced_digits():
            pass
        self.forced = copy.deepcopy(self.value)

    def marked_tex_output(self):
        if len(self.data) == 0 or not self.valid:
            return
        write_tex(self.filename + '_marked.tex', self.marked, 0)

    def _marked_tex_output(self):
        # print(self.value)
        if len(self.data) == 0 or not self.valid:
            return
        for x in range(1, 10):
            for y in range(1, 10):
                if self.value[x - 1, y - 1] != 0:
                    pass
                else:
                    s = self._get_row_digits(x, self.value) + self._get_col_digits(y, self.value) \
                        + self._get_box_digits(x, y, self.value)
                    # print(s)
                    # print(type(s))
                    possible_digits = []
                    for i in range(1, 10):
                        if i not in s:
                            possible_digits.append(i)
                    self.value[x - 1][y - 1] = possible_digits
        self.marked = copy.deepcopy(self.value)
        # print(self.value)

    def worked_tex_output(self):
        if len(self.data) == 0 or not self.valid:
            return
        self.worked = copy.deepcopy(self.marked)

        for x in range(9):
            for y in range(9):
                cell_worked = self.value[x, y]
                cell_marked = self.marked[x, y]
                if isinstance(cell_marked, list):
                    self.worked[x, y] = []
                    for digit in range(1, 10):
                        if isinstance(cell_worked, list):  # cell not done
                            if digit in cell_marked and digit not in cell_worked:
                                self.worked[x, y].append(float(digit))
                            elif digit in cell_marked and digit in cell_worked:
                                self.worked[x, y].append(digit)
                        else:  # cell done
                            if digit in cell_marked and digit != cell_worked:
                                self.worked[x, y].append(float(digit))
                            elif digit in cell_marked and digit == cell_worked:
                                self.worked[x, y].append(digit)

        # print('worked',self.worked)
        write_tex(self.filename + '_worked.tex', self.worked, 1)

    def _worked_tex_output(self):

        if len(self.data) == 0 or not self.valid:
            return
        while self._get_preemptive_set() and self._cross_out_digits():
            pass
            # print("crossing out")

        self.worked = copy.deepcopy(self.value)

    def _fill_in_forced_digits(self):
        progress = False
        freq_l = self._get_freq_digits(self.data)
        # print('freq',freq_l)
        for d in freq_l:
            # print('d=',d)
            for box_i in range(3):
                for box_j in range(3):
                    box = copy.deepcopy(self.value[3 * box_i:3 * (box_i + 1), 3 * box_j:3 * (box_j + 1)])
                    box_nums = []
                    # print('raw_box',box)
                    if d in box:
                        pass
                    else:
                        for i in range(3):
                            for j in range(3):
                                x = 3 * box_i + i
                                y = 3 * box_j + j
                                if box[i, j] == 0:
                                    row = self._get_row_digits(x + 1, self.value)
                                    col = self._get_col_digits(y + 1, self.value)
                                    # print('row',x,row)
                                    # print('col',y,col)
                                    if d in row or d in col:
                                        box[i, j] = -1
                        # print('taged_box',box)

                        for b_row in box: box_nums = box_nums + b_row.tolist()
                        if box_nums.count(0) == 1:
                            for i in range(3):
                                for j in range(3):
                                    if box[i, j] == 0:
                                        x = 3 * box_i + i
                                        y = 3 * box_j + j
                                        self.value[x, y] = d
                                        progress = True
        return progress

    def _get_freq_digits(self, data):
        dic = {}
        for i in range(1, 10): dic[i] = data.count(i)
        freq_l = []
        times = list(dic.values())
        times.sort()
        for i in times:  # find the most freqent digit
            for j in range(1, 10):
                if i == dic[j] and j not in freq_l:
                    freq_l.append(j)
        freq_l.reverse()
        return freq_l

    def _get_row_digits(self, x, barray):
        return barray[x - 1, :].tolist()

    def _get_col_digits(self, y, barray):
        return barray[:, y - 1].tolist()

    def _get_box_digits(self, x, y, barray):
        if x in [1, 2, 3] and y in [1, 2, 3]:  # box1
            box = barray[0:3, 0:3]
        elif x in [1, 2, 3] and y in [4, 5, 6]:  # box2
            box = barray[0:3, 3:6]
        elif x in [1, 2, 3] and y in [7, 8, 9]:  # box3
            box = barray[0:3, 6:9]
        elif x in [4, 5, 6] and y in [1, 2, 3]:  # box4
            box = barray[3:6, 0:3]
        elif x in [4, 5, 6] and y in [4, 5, 6]:  # box5
            box = barray[3:6, 3:6]
        elif x in [4, 5, 6] and y in [7, 8, 9]:  # box6
            box = barray[3:6, 6:9]
        elif x in [7, 8, 9] and y in [1, 2, 3]:  # box7
            box = barray[6:9, 0:3]
        elif x in [7, 8, 9] and y in [4, 5, 6]:  # box8
            box = barray[6:9, 3:6]
        elif x in [7, 8, 9] and y in [7, 8, 9]:  # box9
            box = barray[6:9, 6:9]
        # print(box)
        return box[0].tolist() + box[1].tolist() + box[2].tolist()

    def _get_preemptive_set(self):
        progress = False
        for m in range(2, 5):
            coms = list(combinations([i for i in range(1, 10)], m))
            # print("combine",coms)
            for x in range(9):
                for com in coms:  # search for preemptive set
                    cnt = 0
                    union = []
                    loc_record = []
                    for y in range(9):
                        cell = self.value[x, y]
                        if isinstance(cell, list) and 2 <= len(cell) <= m and set(cell).issubset(set(com)):
                            cnt += 1
                            union = union + cell
                            loc_record.append([x, y])

                    if cnt == m and set(union) == set(com):
                        prp = preem()
                        prp.dimension = 'row'
                        prp.digits = list(com)
                        prp.locat = loc_record
                        self.prplist.append(prp)
                        progress = True

            for y in range(9):
                for com in coms:
                    cnt = 0
                    union = []
                    loc_record = []
                    for x in range(9):
                        cell = self.value[x, y]
                        if isinstance(cell, list) and 2 <= len(cell) <= m and set(cell).issubset(set(com)):
                            cnt += 1
                            union = union + cell
                            loc_record.append([x, y])
                    if cnt == m and set(union) == set(com):
                        prp = preem()
                        prp.dimension = 'col'
                        prp.digits = list(com)
                        prp.locat = loc_record
                        self.prplist.append(prp)
                        progress = True

            for box_i in range(3):
                for box_j in range(3):
                    for com in coms:
                        cnt = 0
                        union = []
                        loc_record = []
                        for i in range(3):
                            for j in range(3):
                                x = 3 * box_i + i
                                y = 3 * box_j + j
                                cell = self.value[x, y]
                                if isinstance(cell, list) and 2 <= len(cell) <= m and set(cell).issubset(set(com)):
                                    cnt += 1
                                    union = union + cell
                                    loc_record.append([x, y])
                        if cnt == m and set(union) == set(com):
                            prp = preem()
                            prp.dimension = 'box'
                            prp.digits = list(com)
                            prp.locat = loc_record
                            self.prplist.append(prp)
                            progress = True
        for x in range(9):
            for y in range(9):
                cell = self.value[x, y]
                if isinstance(cell, list) and len(cell) == 1:
                    prp = preem()
                    prp.dimension = 'all'
                    prp.digits = cell
                    prp.locat.append([x, y])
                    self.prplist.append(prp)
                    progress = True

        return progress

    def _cross_out_digits(self):
        progress = False
        # print("len of prp list",len(self.prplist))
        for i in range(len(self.prplist)):
            prp = self.prplist.pop()
            # print("prp:",prp.digits,prp.locat,prp.dimension)

            if prp.dimension == 'all':  # cross out digits by single on all three dimension
                x = prp.locat[0][0]  # delete digit in same row
                for y in range(9):
                    cell = self.value[x, y]
                    if [x, y] not in prp.locat and isinstance(cell, list):
                        for each in cell:
                            if each == prp.digits[0]:
                                if len(cell) > 1:
                                    cell.remove(each)
                                    progress = True
                y = prp.locat[0][1]  # delete digit in same col
                for x in range(9):
                    cell = self.value[x, y]
                    if [x, y] not in prp.locat and isinstance(cell, list):
                        for each in cell:
                            if each == prp.digits[0]:
                                if len(cell) > 1:
                                    cell.remove(each)
                                    progress = True
                b_x = prp.locat[0][0] // 3  # delete digit in same box
                b_y = prp.locat[0][1] // 3
                for i in range(3):
                    for j in range(3):
                        x = 3 * b_x + i
                        y = 3 * b_y + j
                        cell = self.value[x, y]
                        if [x, y] not in prp.locat and isinstance(cell, list):
                            for each in cell:
                                if each == prp.digits[0]:
                                    if len(cell) > 1:
                                        cell.remove(each)
                                        progress = True
                cell = self.value[prp.locat[0][0], prp.locat[0][1]]
                self.value[prp.locat[0][0], prp.locat[0][1]] = cell[0]

                # for x in range(9):
                #     for y in range(9):
                #         cell = self.value[x,y]
                #         if isinstance(cell,list) and len(cell)==1:
                #             self.value[x,y] = cell[0]

            elif prp.dimension == 'row':  # cross out digits by preemptive set on row
                x = prp.locat[0][0]
                for y in range(9):
                    cell = self.value[x, y]
                    if [x, y] not in prp.locat and isinstance(cell, list):
                        for each in cell:
                            if each in prp.digits:
                                if len(cell) > 1:
                                    cell.remove(each)
                                    progress = True
            elif prp.dimension == 'col':  # cross out on col
                y = prp.locat[0][1]
                for x in range(9):
                    cell = self.value[x, y]
                    if [x, y] not in prp.locat and isinstance(cell, list):
                        for each in cell:
                            if each in prp.digits:
                                if len(cell) > 1:
                                    cell.remove(each)
                                    progress = True
            elif prp.dimension == 'box':  # cross out on box
                b_x = prp.locat[0][0] // 3
                b_y = prp.locat[0][1] // 3
                for i in range(3):
                    for j in range(3):
                        x = 3 * b_x + i
                        y = 3 * b_y + j
                        cell = self.value[x, y]
                        if [x, y] not in prp.locat and isinstance(cell, list):
                            for each in cell:
                                if each in prp.digits:
                                    if len(cell) > 1:
                                        cell.remove(each)
                                        progress = True

        # print("len of prp list",len(self.prplist))
        # print(self.value)
        return progress
