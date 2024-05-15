pki = [("User1", "CA3"),("User2","CA2"),("User3", "CA6"), ("User4","CA4"),("CA3","Root CA"), ("CA4", "CA3")]


def is_trustworthy(user):
    chain_of_trust = make_chain_of_trust(user,  [user])
    if  chain_of_trust[-1] == "Root CA":
        return True, chain_of_trust
    else:
        return False, chain_of_trust

def make_chain_of_trust(user, chain_of_trust):
    for certificate in pki:
        if certificate[0] == user:
            chain_of_trust.append(certificate[1])
            if(certificate[1]!="Root CA"):
                make_chain_of_trust(certificate[1], chain_of_trust)
    return chain_of_trust

User = "User4"

trustworthy, chain_of_trust = is_trustworthy(User)
print("Is", User, "trustworthy?", trustworthy)
print("Chain_of_trust^", chain_of_trust)