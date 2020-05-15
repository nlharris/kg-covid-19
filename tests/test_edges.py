import unittest

import pandas as pd

from kg_covid_19.edges import make_edges, tsv_to_df, has_disconnected_nodes, \
    make_negative_edges


class TestEdges(unittest.TestCase):
    def setUp(self) -> None:
        self.small_nodes_file = 'tests/resources/edges/small_graph_nodes.tsv'
        self.small_edges_file = 'tests/resources/edges/small_graph_edges.tsv'

    def test_tsv_to_df(self):
        df = tsv_to_df(self.small_edges_file)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual((21, 5), df.shape)
        self.assertEqual(df['subject'][0], 'g1')

    def test_make_edges(self):
        self.assertTrue(True)

    def test_has_disconnected_nodes(self):
        edges = tsv_to_df(self.small_edges_file)
        nodes = tsv_to_df(self.small_nodes_file)
        nodes_extra = tsv_to_df('tests/resources/edges/small_graph_nodes_EXTRA_IDS.tsv')
        self.assertTrue(not has_disconnected_nodes(edges_df=edges, nodes_df=nodes))
        self.assertTrue(has_disconnected_nodes(edges_df=edges, nodes_df=nodes_extra))

    def test_make_negative_edges(self):
        num_edges = 5
        edges = tsv_to_df(self.small_edges_file)
        nodes = tsv_to_df(self.small_nodes_file)

        df = make_negative_edges(num_edges=num_edges, edges_df=edges, nodes_df=nodes)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(num_edges, df.shape[0])
        self.assertEqual(edges.shape[1], df.shape[1])
        self.assertListEqual(list(edges.columns), list(df.columns))
        # node_types


