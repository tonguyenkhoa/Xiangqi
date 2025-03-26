import subprocess
import time
# import random

engine_path = '/home/mihari/CODE/Python/Xiangqi/pikafish_ai/Pikafish/src/pikafish'

class AI:
    def __init__(self, engine_path, level):
        self.engine_path = engine_path
        self.level = level

    def get_ai_move(self, fen):
        process = subprocess.Popen(
            [self.engine_path],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True
        )

        # Send command to engine
        # process.stdin.write(f'{self.level}')
        process.stdin.write(f'position fen {fen}\n')
        process.stdin.write(f'{self.level}')
        process.stdin.flush()
        time.sleep(1)
        
        # best_move = None
        # moves = []
        # for line in iter(process.stdout.readline, ''):
        #     line = line.strip()
        #     if line.startswith('info depth'):
        #         move = line.split()[-1]  
        #         moves.append(move)
        #     elif line.startswith('bestmove'):
        #         moves.append(line.split()[1])
        #         break
        # if moves:
        #     best_move = random.choice(moves)

        best_move = None
        for line in iter(process.stdout.readline, ''):
            line = line.strip()
            if "score mate 0" in line:
                break
            if line.startswith('bestmove'):
                best_move = line.split()[1]
                break
            
        # Close engine
        process.stdin.write("quit\n")
        process.stdin.flush()
        process.terminate()
        process.wait()

        return best_move
