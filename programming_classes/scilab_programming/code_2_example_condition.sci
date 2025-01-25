side = input("Tell me the size of the rooms side");

if (side > 0) then
    area = side * side;
    printf("The rooms area is %f", area);
else
    printf("The value %f informed is invalid");
end

n1 = input("Inform a number: ");
n2 = input("Inform a second number: ");

//if (n1 ~= n2) then different
// if (n1 > n2) then
// if (n1 < n2) then
// if (n1 >= n2) then
// if (n1 <= n2) then
if (n1 == n2) then
    printf("The numbers given are equal");
else
    printf("The numbers given are different");
end


