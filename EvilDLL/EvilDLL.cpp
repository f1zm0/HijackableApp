#pragma comment(linker,"/export:AddOne=helpers_orig.AddOne,@1")
#pragma comment(linker,"/export:SubtractOne=helpers_orig.SubtractOne,@2")

#include <windows.h>

void PopCalc()
{
    STARTUPINFO si = { sizeof(si) };
    PROCESS_INFORMATION pi;
    WCHAR cmd[] = L"calc.exe";

    CreateProcess(NULL, cmd, NULL, NULL, 0, 0, NULL, NULL, &si, &pi);
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
    switch (fdwReason)
    {
    case DLL_PROCESS_ATTACH:
        PopCalc();
        break;
    case DLL_THREAD_ATTACH:
        break;
    case DLL_THREAD_DETACH:
        break;
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}