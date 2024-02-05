init python:

    import random
    import copy

    class LoopyLoopLoop:

        def __init__(self, dim, tileset = None):

            self.dim = dim

            if tileset:

                self.tileset = tileset

            else:

                self.num = -1
                self.generator = LoopyTilesetGenerator(dim = dim)
                self.tileset = self.generator.tileset
                self.shuffle()

            self.break_happened = (0,0)

            self.image = [
            "images/loop0.png",
            "images/loop1.png",
            "images/loop2.png",
            "images/loop3.png",
            "images/loop4.png"
            ]

        def next_tileset(self):

            self.num += 1

            self.tileset = self.generator.wip_tilesets[self.num]

        def prev_tileset(self):

            self.num -= 1

            self.tileset = self.generator.wip_tilesets[self.num]

        def shuffle(self):

            for i in range(self.dim[0]):

                for j in range(self.dim[1]):

                    if self.tileset[i][j]:

                        self.tileset[i][j].angle = random.randint(0,3)

        def is_solved(self):

            for i in range(self.dim[0]):

                for j in range(self.dim[1]):

                    if self.tileset[i][j]:

                        self.break_happened = (i,j)

                        cons = self.tileset[i][j].get_connections()

                        for con in cons:

                            if con == 0:

                                if j == self.dim[1] - 1:

                                    return False

                                if not self.tileset[i][j + 1]:

                                    return False
                                
                                elif not self.tileset[i][j + 1].connected_to(num = 2):

                                    return False
                                    
                            elif con == 1:

                                if i == self.dim[0] - 1:

                                    return False

                                if not self.tileset[i + 1][j]:

                                    return False
                                
                                elif not self.tileset[i + 1][j].connected_to(num = 3):

                                    return False

                            elif con == 2:

                                if j == 0:

                                    return False

                                if not self.tileset[i][j - 1]:

                                    return False
                                
                                elif not self.tileset[i][j - 1].connected_to(num = 0):

                                    return False

                            else:

                                if i == 0:

                                    return False

                                if not self.tileset[i - 1][j]:

                                    return False
                                
                                elif not self.tileset[i - 1][j].connected_to(num = 1):

                                    return False

            return True

    class LoopyGenerator:

        def __init__(self, dim):

            self.tileset = []

            self.dim = dim

            self.tileset_size = dim[0] * dim[1]

            self.num_of_start_points = random.randint(1, self.tileset_size // 10 + 1)

            self.weights = [2,6,5,4,3]

            self.connection_list = []

            for weight in self.weights:

                weight += random.randint(-1, 1)

            for i in range(dim[0]):

                self.tileset.append([])

                for j in range(dim[1]):

                    self.tileset[i].append(None)

            self.start_positions = []

            for i in range(self.num_of_start_points):

                self.start_positions.append([random.randint(0, dim[0] - 1), random.randint(0, dim[1] - 1)])

                self.fill(self.start_positions[-1])


        def fill(self, pos):

            if pos[0] >= 0 and pos[0] <= self.dim[0] - 1 and pos[1] >= 0 and pos[1] <= self.dim[1] - 1:


                if self.tileset[pos[0]][pos[1]]:

                    return

                else:

                    connections = []

                    if pos[1] < self.dim[1] - 1:

                        if self.tileset[pos[0]][pos[1] + 1]:

                            if self.tileset[pos[0]][pos[1] + 1] and self.tileset[pos[0]][pos[1] + 1].connected_to(num = 2):

                                connections.append(0)

                        elif random.randint(0,10) > 4:

                                connections.append(0)

                    if pos[0] < self.dim[0] - 1: 

                        if self.tileset[pos[0] + 1][pos[1]] and self.tileset[pos[0] + 1][pos[1]].connected_to(num = 3):

                            connections.append(1)

                        elif random.randint(0,10) > 4:

                                connections.append(1)

                    if pos[1] > 0:

                        if self.tileset[pos[0]][pos[1] - 1] and self.tileset[pos[0]][pos[1] - 1].connected_to(num = 0):

                            connections.append(2)

                        elif random.randint(0,10) > 4:

                                connections.append(2)

                    if pos[0] > 0:

                        if self.tileset[pos[0] - 1][pos[1]] and self.tileset[pos[0] - 1][pos[1]].connected_to(num = 1):

                            connections.append(3)

                        elif random.randint(0,10) > 4:

                                connections.append(3)


                    if len(connections) == 1:

                        self.tileset[pos[0]][pos[1]] = LoopyTile(code = 1, ang = connections[0] - 3)

                    if len(connections) == 2:

                        if (connections[1] + connections[0]) % 2 == 1:

                            self.tileset[pos[0]][pos[1]] = LoopyTile(code = 2, ang = connections[1] if connections[1] == connections[0] + 1 else 0 )

                        else:

                            self.tileset[pos[0]][pos[1]] = LoopyTile(code = 0, ang = connections[0] - 1)

                    if len(connections) == 3:

                        self.tileset[pos[0]][pos[1]] = LoopyTile(code = 3, ang = connections[0])

                    if len(connections) == 4:

                        self.tileset[pos[0]][pos[1]] = LoopyTile(code = 4, ang = 0)

                    for con in connections:

                        if con == 0:
                            
                            self.fill(pos = (pos[0], pos[1] + 1))

                        elif con == 1:
                            
                            self.fill(pos = (pos[0] - 1, pos[1]))

                        elif con == 2:

                            self.fill(pos = (pos[0], pos[1] - 1))

                        else:

                            self.fill(pos = (pos[0] + 1, pos[1]))

                    #self.connection_list.append(connections)

                    return


            return

    class LoopyTilesetGenerator:

        def __init__(self, dim):

            self.position_stack = []

            self.new_position_stack = []

            self.tileset = []

            self.wip_tilesets = []

            for i in range(dim[0]):

                self.tileset.append([])

                for j in range(dim[1]):

                    self.tileset[i].append(None)

            self.dim = dim

            self.size = dim[0] * dim[1]

            self.num_of_starts = random.randint(1, self.size//10 + 1)

            #self.num_of_starts = 1

            for i in range(self.num_of_starts):

                self.fill(pos = (random.randint(0, dim[0] - 1), random.randint(0, dim[1] - 1)))

            while self.filled() < 0.5:

                self.fill(pos = (random.randint(0, dim[0] - 1), random.randint(0, dim[1] - 1)))



            return

        def filled(self):

            pomnum = 0

            for i in range(self.dim[0]):

                for j in range(self.dim[1]):

                    if self.tileset[i][j]:

                        pomnum += 1

            return pomnum / self.size

        def fill(self, pos):

            self.position_stack.append(pos)

            self.use_stack()

            return


        def use_stack(self):

            for pos in self.position_stack:

                self.set_tile(i = pos[0], j = pos[1])

            self.wip_tilesets.append(copy.deepcopy(self.tileset))

            if len(self.new_position_stack):
                
                self.position_stack = self.new_position_stack
                self.new_position_stack = []
                self.use_stack()

            return


        def set_tile(self, i, j):

            if i >= 0 and i <= self.dim[0] - 1 and j >= 0 and j <= self.dim[1] - 1:

                if self.tileset[i][j]:

                    return

                else:

                    connections = []

                    if j < self.dim[1] - 1:

                        if self.tileset[i][j + 1]:

                            if self.tileset[i][j + 1].connected_to(num = 2):

                                connections.append(0)

                        elif random.randint(0,1):

                            connections.append(0)


                    if i < self.dim[0] - 1: 

                        if self.tileset[i + 1][j]:

                            if self.tileset[i + 1][j].connected_to(num = 3):

                                connections.append(1)

                        elif random.randint(0,1):

                                connections.append(1)

                    if j > 0:

                        if self.tileset[i][j - 1]:

                            if self.tileset[i][j - 1].connected_to(num = 0):

                                connections.append(2)

                        elif random.randint(0,1):

                                connections.append(2)

                    if i > 0:

                        if self.tileset[i - 1][j]:

                            if self.tileset[i - 1][j].connected_to(num = 1):

                                connections.append(3)

                        elif random.randint(0,1):

                                connections.append(3)


                    if len(connections) == 1:

                        self.tileset[i][j] = LoopyTile(code = 1, ang = connections[0] - 1)

                    if len(connections) == 2:

                        if (connections[1] + connections[0]) % 2 == 1:

                            self.tileset[i][j] = LoopyTile(code = 2, ang = connections[0] if connections[1] == connections[0] + 1 else 3 )

                        else:

                            self.tileset[i][j] = LoopyTile(code = 0, ang = connections[0] - 1)

                    if len(connections) == 3:

                        pomsum = connections[0] + connections[1] + connections[2]

                        pomang = {
                        3 : 0,
                        4 : 3,
                        5 : 2,
                        6 : 1
                        }

                        self.tileset[i][j] = LoopyTile(code = 3, ang = pomang[pomsum])

                    if len(connections) == 4:

                        self.tileset[i][j] = LoopyTile(code = 4, ang = 0)

                    for con in connections:

                        if con == 0:

                            self.new_position_stack.append((i, j + 1))

                        elif con == 1:
                            
                            self.new_position_stack.append((i + 1, j))

                        elif con == 2:

                            self.new_position_stack.append((i, j - 1))

                        else:

                            self.new_position_stack.append((i - 1, j))

                    #self.connection_list.append(connections)

                    return


            return

    class LoopyTile:

        def __init__(self, code, ang):

            self.code = code

            self.connections = None

            self.define_connections()

            self.angle = ang

            self.anim = 0

        def define_connections(self):

            if self.code == 0:

                self.connections = [1,3]

            elif self.code == 1:

                self.connections = [1]

            elif self.code == 2:

                self.connections = [0,1]

            elif self.code == 3:

                self.connections = [0,1,2]

            else:

                self.connections = [0,1,2,3]

            return


        def get_connections(self):

            pomcon = []

            for con in self.connections:

                pomcon.append((con + self.angle) % 4) 

            return pomcon


        def connected_to(self, num):

            for con in self.connections:

                if (con + self.angle) % 4 == num:

                    return True

            return False


        def rotate90(self):

            self.angle += 1
            self.anim = 1

            return



            


