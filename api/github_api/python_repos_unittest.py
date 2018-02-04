import unittest
import python_repos as pr

class PythonResponeTest(unittest.TestCase):

    def setUp(self):
        self.res = pr.get_reponse()
        self.repo_dicts = pr.get_repo_dicts(self.res)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)

    def test_get_response(self):
        self.assertEqual(self.res.status_code, 200)

    def test_repo_dicts(self):
        self.assertEqual(len(self.repo_dicts), 30)

        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())


if __name__ == '__main__':
    unittest.main()