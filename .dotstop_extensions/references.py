import requests
from trudag.dotstop.core.reference.references import BaseReference
import re
import os
import pathlib


def find_test_lines(test_name, cpp_file_content):
    pattern = rf'.*?(SECTION\("{re.escape(test_name)}"\))'

    # Substitute everything before the target with just the matched SECTION(dummy_test)
    text_after_section = re.sub(pattern, r'\1', cpp_file_content, flags=re.DOTALL)

    counter = 0
    seen_first_opening_bracet = False
    for index, char in enumerate(text_after_section):
        if char == '{':
          seen_first_opening_bracet = True
          counter +=1
        elif char == '}':
          counter -=1
        if counter == 0 and seen_first_opening_bracet:
          return text_after_section[:index+1]


class CPPReference(BaseReference):
    def language():
        return "cpp"

    def type():
        return "cpp-test"

    def __init__(self, path, test_name):
        self.path = path
        self.test_name = test_name
        self.code = self.parse_test()

    def parse_test(self):
        filepath = pathlib.Path(os.getcwd()) / pathlib.Path(self.path)
        contents = ""
        with open(filepath, "r") as f:
            contents = f.read()
            self.code = find_test_lines(self.test_name, contents)

    @property
    def content(self):
        return self.code

    def as_markdown(self, filepath=None):
        # This is basically just pretty-printing for `self.content` Importantly,
        # you should use code fences to specify that formatting.
        # `Filepath` is the path to the report being rendered. This is so that
        # we can copy supporting files to be local to there , for example
        return fence_code_block(self.content.decode(), type(self).language())

    def __str__(self):
        return escape_angled_braces(
            f"{self.path} : ({self.span[0]}) - ({self.span[1]})"
        )

# if __name__ == "__main__":
#     test_name = "dummy_test"
#     cpp_file_content = """

# TEST_CASE("algorithms")
# {
#     json j_array = {13, 29, 3, {{"one", 1}, {"two", 2}}, true, false, {1, 2, 3}, "foo", "baz"};
#     json j_object = {{"one", 1}, {"two", 2}};

#     SECTION("dummy_test")
#     {
#         SECTION("std::all_of")
#         {
#             CHECK(std::all_of(j_array.begin(), j_array.end(), [](const json & value)
#             {
#                 return !value.empty();
#             }));
#             CHECK(std::all_of(j_object.begin(), j_object.end(), [](const json & value)
#             {
#                 return value.type() == json::value_t::number_integer;
#             }));
#         }
#     }
# }



#     """


#     print(find_test_lines(test_name, cpp_file_content))
