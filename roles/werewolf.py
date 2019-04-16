import role

class Werewolf(role.Role):
    RoleName = "Werewolf"
    RoleTeam = "Werewolf"
    def action(self,list_players):
        string = ""
        for i in list_players:
            if i.RoleName == "Werewolf":
                string += i.RoleName
                string += ", "
        return string

