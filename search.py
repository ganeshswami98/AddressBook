$data = mysql_query("SELECT * FROM address ORDER BY name ASC")
or die(mysql_error());
Print "<h2>Address Book</h2><p>";
Print "<table border cellpadding=3>";
Print "<tr><th width=100>Name</th><th width=100>Phone</th><th width=200>Email</th><th width=100 colspan=2>Admin</th></tr>"; Print "<td colspan=5 align=right><a href=" .$_SERVER[’PHP_SELF’]. "?mode=add>Add Contact</a></td>";
while($info = mysql_fetch_array( $data ))
{
Print "<tr><td>".$info['name'] . "</td> ";
Print "<td>".$info['phone'] . "</td> ";
Print "<td> <a href=mailto:".$info['email'] . ">" .$info['email'] . "</a></td>";
Print "<td><a href=" .$_SERVER[’PHP_SELF’]. "?id=" . $info['id'] ."&name=" . $info['name'] . "&phone=" . $info['phone'] ."&email=" . $info['email'] . "&mode=edit>Edit</a></td>"; Print "<td><a href=" .$_SERVER[’PHP_SELF’]. "?id=" . $info['id'] ."&mode=remove>Remove</a></td></tr>";
}
Print "</table>";