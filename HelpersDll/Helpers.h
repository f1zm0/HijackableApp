#pragma once

#define HELPERS_API __declspec(dllexport)


extern "C" HELPERS_API int AddOne(int a);

extern "C" HELPERS_API int SubtractOne(int a);
