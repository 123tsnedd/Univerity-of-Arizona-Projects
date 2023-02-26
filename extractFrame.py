'''
Author: Trevor Snedden
Date: 12/06 /22
Professor: Dr. Ageel
Class: APCV 320
Assignment: FINAL

Description:

You will be creating a Python program saved in a file named "extractFrame.py". The Python program
will read text from a file named "wireShark.txt" and display the frames with essential frame data. For
each frame, you need to extract and present its frame number, the source and destination
addresses, as well as the frame type. The frame number always appears after "Frame" at the
beginning of each frame in the document. For either source or destination address, it is composed of
12 hexadecimal digits, every two of which are separated by colon. The address examples could be
like below:
00:14:ee:08:dd:b1
01:00:5e:7f:ff:fa
result should look like below. each on new line.
Frame 1, Src:00:14:ee:08:dd:b1, Dst:01:00:5e:7f:ff:fa, Type:0x0800
'''

import re

def sep_line(extracted):
    '''Function separates and cleans list to string of rows for each Frame.
    Returns new string'''
    string = ''
    for x in extracted:
        if 'Type' not in x:
            string += x+','
        else:
            string += x
    return string.rstrip('\n')


def extract_block(file): #extracts data from chunk and returns to file_manager to enter into new file
    '''Function extracts Frame, Src, Dst, and Type along with respective info. passes to sep_line()for cleaning. returns data to file_manager'''
    extracted = []
    find_frame = re.compile(r'Frame\s\d')
    find_hexi = re.compile(r'[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]{2}')
    find_type = re.compile(r'\d[x]\d\d\d\d?')
    for line in file:
        matching = find_hexi.findall(line)
        frame = find_frame.findall(line)
        found_type = find_type.findall(line)
        if frame:
            extracted += frame
            #extracted += matching
        if 'Src:' in line and matching:
            extracted += [' Src: ' + matching[0] if matching else '']
        if 'Dst:' in line and matching:
            extracted += [' Dst: ' + matching[1] if matching else '']
        elif 'Type:' in line and found_type:
            extracted += [' Type: ' + found_type[0]+'\n']
    extracted = sep_line(extracted)
    return extracted


def file_manager(file): #opens and creates/writes new file.
    '''Function opens file to send to extract_block() and writes/creates a new file with data that is returned.'''
    with open(file,'r') as og_file:
        extraction = extract_block(og_file)
    return extraction
        # with open('extract_'+file, 'w') as extracted_file:
        #     extracted_file.write(extract_block(og_file))


def main():

    Frame_data = file_manager('wireShark.txt')
    print(Frame_data)


if __name__ == '__main__':
    main()
