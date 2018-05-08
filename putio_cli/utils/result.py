import json

from prettytable import PrettyTable

from putio_cli.utils.text import add_title_to_table


class BaseResult:
    def __init__(self, name, columns, results=None):
        assert isinstance(name, str), "name must be a string"
        self.name = name
        assert isinstance(columns, list), "columns must be of type list"
        self.columns = columns
        if results:
            assert isinstance(results, list), "results must be of type ist"
            assert isinstance(results[0], list), "results must be a list of lists"
            assert all(len(columns) == len(result) for result in results), \
                "length of all results must be equal to the length of columns"
            assert all(len(result) == len(results[0]) for result in results), \
                "All elements of results must have the same length"
            self.results = results
        else:
            self.results = []

    def add_result(self, new_res):
        assert isinstance(new_res, list), "new_res must be of type list"
        if self.results:
            assert len(new_res) == len(self.results[0]), "new_res must be the same len as the other elements in results"
        else:
            assert len(new_res) == len(self.columns), "length of new_res must be equal to length of columns"
        self.results.append(new_res)

    def _show_table(self):
        table = PrettyTable(field_names=self.columns)
        for row in self.results:
            table.add_row(row)
        retval = add_title_to_table(table, self.name)
        return retval

    def _show_json(self):
        results = {"results": [],
                   "title": self.name}
        formatted_result = {"result": []}
        for result in self.results:
            row_res = {}
            for prop, value in zip(self.columns, result):
                row_res[prop] = value
            formatted_result['result'].append(row_res)
        results['results'].append(formatted_result)
        return json.dumps(results)

    def show(self, formatter):
        assert len(self.results) > 0, "You need at least one value in results to show (call add_result at least once)"
        assert formatter in ["json", "table"], "formatter has be to either 'json' or 'table'"
        if formatter == "table":
            return self._show_table()
        elif formatter == "json":
            return self._show_json()


class MultiResult(BaseResult):
    def __init__(self, name, columns, results=None):
        BaseResult.__init__(name, columns, results)

    def _show_table(self):
        table = PrettyTable(field_names=self.columns)
        for row in self.results:
            table.add_row(row)
        retval = add_title_to_table(table, self.name)

        final_res = []
        all_table = retval.split('\n')
        for line in all_table:
            final_line = []
            if all(field.isspace() or field == '' for field in line.split('|')):
                for field in line.split('|'):
                    final_line.append(field.replace(' ', '-'))
                final_line = '|'.join(final_line)
            if final_line:
                final_res.append(final_line)
            else:
                final_res.append(line)
        return '\n'.join(final_res)

    def _show_json(self):
        results = {"results": [],
                   "title": self.name}
        formatted_result = {"result": []}
        for result in self.results:
            if all(element == '' for element in result):
                continue
            row_res = {}
            for prop, value in zip(self.columns, result):
                row_res[prop] = value
            formatted_result['result'].append(row_res)
        results['results'].append(formatted_result)
        return json.dumps(results)
