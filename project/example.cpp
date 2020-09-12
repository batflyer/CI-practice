// Example came out of:
// https://dzone.com/articles/how-to-use-the-newest-c-string-conversion-routines
// Tutorials are likely licensed in some way, but I did not check.

#include <charconv>
#include <string>
#include <iostream>

int main() {

  const std::string str1 { "123" };
  int value = 0;

  const auto res = std::from_chars(
    str1.data(),
    str1.data() + str1.size(),
    value
  );

  if (res.ec == std::errc()) {
    std::cout << "value: " << value << ", distance: " << res.ptr - str1.data() << '\n';
  } else if (res.ec == std::errc::invalid_argument) {
    std::cout << "invalid argument!\n";
  } else if (res.ec == std::errc::result_out_of_range) {
    std::cout << "out of range! res.ptr distance: " << res.ptr - str1.data() << '\n';
  }
}
