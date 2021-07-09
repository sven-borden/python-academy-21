import pygame
import numpy as np

color_about_to_die = (200, 0, 0)
color_alive = (255, 255, 215)
color_background = (10, 10, 40)
color_grid = (30, 30, 60)

'''
color : (rouge [0;255], vert[0;255], bleu[0;255])
'''


def update(surface, cur_cells, sz):
    nxt_cells = np.zeros((cur_cells.shape[0], cur_cells.shape[1]))

    width = cur_cells.shape[0]
    height = cur_cells.shape[1]

    for i in range(1, width-1):
        for j in range(1, height-1):
            '''
            calcule du nombre de voisin vivant autour de la cellule
            '''
            n_v_vivant = 0
            n_v_vivant = n_v_vivant + cur_cells[i-1, j-1]
            n_v_vivant = n_v_vivant + cur_cells[i+1, j+1]
            n_v_vivant = n_v_vivant + cur_cells[i-1, j+1]
            n_v_vivant = n_v_vivant + cur_cells[i+1, j-1]
            n_v_vivant = n_v_vivant + cur_cells[i-1, j]
            n_v_vivant = n_v_vivant + cur_cells[i, j-1]
            n_v_vivant = n_v_vivant + cur_cells[i, j+1]
            n_v_vivant = n_v_vivant + cur_cells[i+1, j]
            
            color = color_background
            
            if n_v_vivant == 3 and cur_cells[i, j] == 0:
                nxt_cells[i, j] = 1
                color = color_alive
            if (n_v_vivant == 2 or n_v_vivant == 3) and cur_cells[i, j] == 1:
                nxt_cells[i, j] = 1
                color = color_alive
            if nxt_cells[i, j] < cur_cells[i, j]:
                color = color_about_to_die
            # if n_v_vivant >= 4:
            #     nxt_cells[i, j] = 0
            # if n_v_vivant <= 1:
            #     nxt_cells[i, j] = 0
            pygame.draw.rect(surface, color, (j*sz, i*sz, sz-1, sz-1))
        







    return nxt_cells



def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
                        
    pos = (3,3)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells

def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    cells = init(dimx, dimy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(color_grid)
        cells = update(surface, cells, cellsize)
        pygame.display.update()

if __name__ == "__main__":
    main(120, 90, 8)