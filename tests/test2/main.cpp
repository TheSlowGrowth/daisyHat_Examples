#include <daisy_seed.h>
#include <daisyHat.h>

daisy::DaisySeed seed;

int main()
{
    seed.Configure();
    seed.Init();

    daisyhat::StartTest(seed, "test2");
    const char* a = "StringA";
    const char* b = "StringB";
    EXPECT_STREQ(a, b);
    daisyhat::FinishTest();
}