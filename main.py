import json
from toolkit import ToolKit
from data import DATASETS
from tasks import TASKS
from agent import Agent

def main():
    print("Initializing ToolKit and Agent...")
    toolkit = ToolKit()
    agent = Agent(toolkit, DATASETS)

    print(f"Loaded {len(TASKS)} tasks.\n")
    
    score = 0
    
    for task in TASKS:
        print(f"Task {task['id']}: {task['goal']}")
        
        try:
            answer = agent.solve(task)
            
            # Simple check
            if answer == task['expected']:
                print(f"  [PASS] Got: {answer}")
                score += 1
            else:
                print(f"  [FAIL] Expected {task['expected']}, got {answer}")
                
            print(f"  Steps taken: {len(agent.history)}")
            
        except Exception as e:
            print(f"  [ERROR] {e}")
            
        print("-" * 50)
        
    print(f"\nFinal Demo Score: {score} / {len(TASKS)}")
    if score == len(TASKS):
        print("Agent is fully operational!")

if __name__ == "__main__":
    main()
