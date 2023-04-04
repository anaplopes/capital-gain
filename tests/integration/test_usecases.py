import json
import unittest
import subprocess


class TestUseCases(unittest.TestCase):

    def load_fixture(self, name):
        """Carrega um arquivo fixture no diretório fixtures."""
        with open(self.fixture_path(name), 'r') as f:
            return json.load(f)

    def fixture_path(self, name):
        """Obtém o caminho completo para um arquivo fixture."""
        return f'tests/fixtures/{name}'

    def test_case_one(self):
        data = self.load_fixture('case_one.json')

        process = subprocess.Popen(
            ['python3', '-m', 'taxcli'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)

        stdout, _ = process.communicate(json.dumps(data["in"]).encode())
        self.assertEqual(json.loads(stdout), data['out'])
        process.terminate()

    def test_case_two(self):
        data = self.load_fixture('case_two.json')

        process = subprocess.Popen(
            ['python3', '-m', 'taxcli'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)

        stdout, _ = process.communicate(json.dumps(data["in"]).encode())
        self.assertEqual(json.loads(stdout), data['out'])
        process.terminate()

    def test_case_three(self):
        data = self.load_fixture('case_three.json')

        process = subprocess.Popen(
            ['python3', '-m', 'taxcli'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)

        stdout, _ = process.communicate(json.dumps(data["in"]).encode())
        self.assertEqual(json.loads(stdout), data['out'])
        process.terminate()

    def test_case_four(self):
        data = self.load_fixture('case_four.json')

        process = subprocess.Popen(
            ['python3', '-m', 'taxcli'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)

        stdout, _ = process.communicate(json.dumps(data["in"]).encode())
        self.assertEqual(json.loads(stdout), data['out'])
        process.terminate()

    def test_case_five(self):
        data = self.load_fixture('case_five.json')

        process = subprocess.Popen(
            ['python3', '-m', 'taxcli'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)

        stdout, _ = process.communicate(json.dumps(data["in"]).encode())
        self.assertEqual(json.loads(stdout), data['out'])
        process.terminate()

    def test_case_six(self):
        data = self.load_fixture('case_six.json')

        process = subprocess.Popen(
            ['python3', '-m', 'taxcli'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)

        stdout, _ = process.communicate(json.dumps(data["in"]).encode())
        self.assertEqual(json.loads(stdout), data['out'])
        process.terminate()

    def test_case_seven(self):
        data = self.load_fixture('case_seven.json')

        process = subprocess.Popen(
            ['python3', '-m', 'taxcli'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)

        stdout, _ = process.communicate(json.dumps(data["in"]).encode())
        self.assertEqual(json.loads(stdout), data['out'])
        process.terminate()

    def test_case_eight(self):
        data = self.load_fixture('case_eight.json')

        process = subprocess.Popen(
            ['python3', '-m', 'taxcli'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)

        stdout, _ = process.communicate(json.dumps(data["in"]).encode())
        self.assertEqual(json.loads(stdout), data['out'])
        process.terminate()


if __name__ == "__name__":
    unittest.main()
