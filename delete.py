if ( $mode=="remove")
{
mysql_query ("DELETE FROM address where id=$id");
Print "Entry has been removed <p>";
}