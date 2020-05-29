
 if ( $mode=="add")
{
Print '<h2>Add Contact</h2>
<p>
<form action=';
echo $PHP_SELF; 
Print '
method=post>
<table>
<tr><td>Name:</td><td><input type="text" name="name" /></td></tr>
<tr><td>Phone:</td><td><input type="text" name="phone" /></td></tr>
<tr><td>Email:</td><td><input type="text" name="email" /></td></tr>
<tr><td colspan="2" align="center"><input type="submit" /></td></tr>
<input type=hidden name=mode value=added>
</table>
</form> <p>';
}
if ( $mode=="added")
{
mysql_query ("INSERT INTO address (name, phone, email) VALUES ('$name', '$phone', '$email')");
}
