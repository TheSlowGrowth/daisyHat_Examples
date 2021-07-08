#include <daisy_seed.h>
#include <daisyHat.h>

daisy::DaisySeed seed;

int main()
{
    seed.Configure();
    seed.Init();

    daisyhat::Init(seed, "Signalling");

    daisyhat::signals::AwaitHostSignal("before_host_delay");
    const auto testStartTime = daisy::System::GetNow();
    daisyhat::signals::AwaitHostSignal("after_host_delay");
    const auto testEndTime = daisy::System::GetNow();

    // expect that the time between two signals is within 10% 
    // from the 500ms that's configured in the host-side test script.
    const auto timePassedInMs = testEndTime - testStartTime;
    EXPECT_NEAR(timePassedInMs, 500, 50);

    // send a signal to the host to test the other direction
    daisy::System::Delay(1000);
    daisyhat::signals::SendSignal("after_seed_delay");

    daisyhat::FinishTest();
}