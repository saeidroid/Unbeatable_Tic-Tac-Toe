import tensorflow as tf
import matplotlib.pyplot as plt

from util import evaluate_players
from tic_tac_toe.TFSessionManager import TFSessionManager
from tic_tac_toe.RandomPlayer import RandomPlayer
from tic_tac_toe.RndMinMaxAgent import RndMinMaxAgent
from tic_tac_toe.DeepExpDoubleDuelQPlayer import DeepExpDoubleDuelQPlayer

TENSORLOG_DIR = './graphs'

if tf.gfile.Exists(TENSORLOG_DIR):
    tf.gfile.DeleteRecursively(TENSORLOG_DIR)

tf.reset_default_graph()

nnplayer = DeepExpDoubleDuelQPlayer("QLearner1")
rndplayer = RandomPlayer()
rm_player = RndMinMaxAgent()

TFSessionManager.set_session(tf.Session())

sess = TFSessionManager.get_session()
writer = tf.summary.FileWriter(TENSORLOG_DIR, sess.graph)
nnplayer.writer = writer

sess.run(tf.global_variables_initializer())



#Let's play the RandomPlayer. The NN player going first to start with:
game_number, p1_wins, p2_wins, draws = evaluate_players(nnplayer, rndplayer, num_battles=500)
#Going second:
#game_number, p1_wins, p2_wins, draws = evaluate_players(rndplayer, nnplayer, num_battles=500)

#Let's play the non-deterministic Min Max player. The NN player going first to start with:
#game_number, p1_wins, p2_wins, draws = evaluate_players(nnplayer, rm_player, num_battles=500, writer=writer)
#Going second:
#game_number, p1_wins, p2_wins, draws = evaluate_players(rm_player, nnplayer, num_battles=500, writer=writer)


writer.close()

p = plt.plot(game_number, draws, 'r-', game_number, p1_wins, 'g-', game_number, p2_wins, 'b-')

plt.show()
TFSessionManager.set_session(None)
