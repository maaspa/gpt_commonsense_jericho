# gpt_commonsense_jericho - INF8225 Project #31 (Maxime Aspros, Ahmed El Shami, and Md Radwan Rahman)

This repository contains the code used to test out the Jericho and TWC environments using ChatGPT. Please note that **`agentpy`** and **`jericho_game.py`** are the only files modified or created. All other files come from the respective GitHub repositories of the following publications:

- [IBM Commonsense RL](https://github.com/IBM/commonsense-rl)
- [Microsoft Jericho](https://github.com/microsoft/jericho)

We do not claim any rights to the original work in these repositories; this project is intended solely for a school class assignment.

---

### Setting Up the Environment

To download the required game for Jericho, execute the following commands within the `jericho_test` folder:

```bash
wget https://github.com/BYU-PCCL/z-machine-games/archive/master.zip
unzip master.zip
```

---

### Running the Project

There are two main functions to run the project:

1. **Running the test agent in the `commonsense-rl` folder**:
   Navigate to the `commonsense-rl` folder and run:

   ```bash
   python -u test_agent.py --agent_type simple --game_dir ./games/twc --game_name *.ulx --difficulty_level easy --split test --nruns 1
   ```

2. **Running the Jericho game in the `jericho_test` folder: Navigate to the `jericho_test` folder and execute**:

```bash
python jericho_game.py
```
