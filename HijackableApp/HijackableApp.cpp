#include <iostream>
#include "Helpers.h"


int main()
{
	try
	{
		std::wcout << L"Result: " << AddOne(1336) << std::endl;
	}
	catch (const std::exception& ex)
	{
		std::wcout << ex.what() << std::endl;
	}

	return EXIT_SUCCESS;
}
