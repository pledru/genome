import subprocess

def process():
    file = open('peak.txt', 'r') 
    lines = file.readlines() 
    i = 0
    list = []
    for line in lines: 
        coordinate = line.strip() # remove the trailing \n

        result = subprocess.run(['./twoBitToFa', 'hg38.2bit:' + coordinate, 'stdout'], stdout=subprocess.PIPE)
        # seq is of the format:
        # b'>chr1:102743-103184\naaagtctatttttcctt...gaatcgcttgaacccaggag\n'
        seq = result.stdout.decode()
        # so process the line
        index = seq.find('\n') # first return is the coordinate
        coord = seq[:index]
        coord = coord[coord.find('>') + 1:]

        seq = seq[index + 1:]
        seq = seq.replace('\n', '') # replace all return by blank
        seq = seq.lower()
        r = coord + ',' + seq + '\n'
        list.append(r)
        i = i + 1
        if i % 1000 == 0:
            print('.', end='', flush=True)

    # save the result
    f = open('result.txt', 'w')
    f.writelines(list)
    f.close()

process()
