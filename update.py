if ( $mode=="edit")
{
Print '<h2>Edit Contact</h2>
<p>
<form action=';
echo $PHP_SELF;
Print '
method=post>
<table>
<tr><td>Name:</td><td><input type="text" value="';
Print $name;
print '" name="name" /></td></tr>
<tr><td>Phone:</td><td><input type="text" value="';
Print $phone;
print '" name="phone" /></td></tr>
<tr><td>Email:</td><td><input type="text" value="';
Print $email;
print '" name="email" /></td></tr>
<tr><td colspan="2" align="center"><input type="submit" /></td></tr>
<input type=hidden name=mode value=edited>
<input type=hidden name=id value=';
Print $id;
print '>
</table>
</form> <p>';
}
if ( $mode=="edited")
{
mysql_query ("UPDATE address SET name = '$name', phone = '$phone', email = '$email' WHERE id = $id");
Print "Data Updated!<p>";
} 