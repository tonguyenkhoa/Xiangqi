import subprocess
import time

def get_ai_move(fen):
    engine_path = '/home/mihari/CODE/Python/Xiangqi/pikafish_ai/Pikafish/src/pikafish'
    process = subprocess.Popen(
        [engine_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    process.stdin.write(f"position fen {fen}\n")
    process.stdin.write("go depth 1\n")
    process.stdin.flush()
    time.sleep(1)
    
    while True:
        output = process.stdout.readline().strip()
        if output.startswith("bestmove"):
            best_move = output.split()[1]
            break
    
    process.stdin.write("quit\n")
    process.stdin.flush()
    process.terminate()
    
    return best_move

fen = "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/4C2C/9/RNBAKABNR b"
best_move = get_ai_move(fen)
print(f"Best move: {best_move}")