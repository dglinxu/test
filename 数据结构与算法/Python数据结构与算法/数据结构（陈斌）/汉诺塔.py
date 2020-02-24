def moveTower(height,fromPole,withPole,toPole):
    if height>=1:
        moveTower(height-1,fromPole,toPole,fromPole)
        moveDisk(height,fromPole,toPole)
        moveTower(height-1,withPole,fromPole,toPole)
def moveDisk(disk,fromPole,toPole):
    print(f'Moving disk[{disk}] from {fromPole} to {toPole}')

moveTower(10,'#1','#2','#3')