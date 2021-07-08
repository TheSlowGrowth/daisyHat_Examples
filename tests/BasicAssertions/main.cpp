#include <daisy_seed.h>
#include <daisyHat.h>

daisy::DaisySeed seed;

int main()
{
    seed.Configure();
    seed.Init();

    daisyhat::Init(seed, "BasicAssertions");

    // compare to integers
    int a = 1;
    int b = 1;
    EXPECT_EQ(a, b);

    // compare floats
    float c = 1.0f;
    float d = 2.0f;
    EXPECT_LT(c, d);

    float e = 1.0f;
    float f = 1.01f;
    EXPECT_NEAR(e, f, 0.02f);
    
    // compare strings
    const char* strA = "a string";
    const char* strB = "a string";
    EXPECT_STREQ(strA, strB);

    // Expect bools
    EXPECT_TRUE(false || true);
    EXPECT_FALSE(false && true);

    daisyhat::FinishTest();
}