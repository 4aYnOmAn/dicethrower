#include <cstdio>
#include <cstring>
#include <iostream>
#include <memory>
#include <string>
#include <list>
#include <iterator>
#include <thread>

std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

std::string clear = exec("clear");

std::string good_print(std::string text) {
    text = "figlet '" + text + "'";
    return exec(text.c_str());
}

void loadthing (int time, int times, int sn, int en) {
    std::cout << clear;
    int endtimes = 0;
    for (int n = 0; n < times; n++) {
        for (int i = 1; i <= sn; i++) {
            if (endtimes > times and i == en) {
                std::cout << good_print("[ " + std::to_string(en) + " ]");
                std::this_thread::sleep_for(std::chrono::milliseconds(time+1000));

                std::cout << clear << std::endl;
                return;
            }
            std::cout << good_print("[ " + std::to_string(i) + " ]");
            std::this_thread::sleep_for(std::chrono::milliseconds(time));

            std::cout << clear << std::endl;
            endtimes +=1;
        }
        time += 0.1;
    }
}

void dice() {
    std::string inp;
    int fn = 0;
    int sn = 0;
    std::cout << "[How many dices?] (num) " << std::endl;
    std::cin >> inp;
    fn = atoi(inp.c_str());
    std::cout << "[Which?] (num) d" << std::endl;
    std::cin >> inp;
    sn = atoi(inp.c_str());
    if (fn == 0 or sn == 0) {
        std::cout << "[!]Not a integer or to small, try again.[!]\n\n";
    }
    std::cout << clear << std::endl;
    if (fn == 1) {
        if (sn <= 100) {
            int en = 1 + rand() % sn;
            loadthing(10/sn*100, 1 + rand() % sn, sn, en);
            std::cout << "[Results]:\n" + good_print(std::to_string(fn) + "d" + std::to_string(sn) + "=" + std::to_string(en) + "\n\n");
        }
        else {
            std::cout << "[Results]:\n" + good_print(std::to_string(fn) + "d" + std::to_string(sn) + "=" + std::to_string(1 + rand() % sn) + "\n\n");
        }
    }
    else {
        if (fn > 999 or sn > 999) {
            std::cout << "[!]To big number, try again, it must be < 1000[!]\n\n";
        }
        else {
            std::list<int> nums;
            int result = 0;
            for (int i; i < fn; i++) {
                int num = 1 + rand() % sn;
                nums.push_back(num);
                result += num;
            }
            std::cout << "[Numbers: ";
            std::copy(nums.begin(), nums.end(), std::ostream_iterator<int>(std::cout,", "));
            std::cout << "]" << "\n" << "[Result]:\n" << good_print(std::to_string(fn) + "d" + std::to_string(sn) + "=" + std::to_string(result)) + "\n\n";
        }
    }
}

int main() {
    while (true) {dice();}
    return 0;
}
