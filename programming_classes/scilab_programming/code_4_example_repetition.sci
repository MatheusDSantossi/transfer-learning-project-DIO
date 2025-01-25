total = 0;
x = input("Type the first number: ");

while(x ~= 0)
    total = total+x;
    x = input("Type one more value or 0 to end the sum: ");
end

printf("The sum of the numbers given is: %d", total);
