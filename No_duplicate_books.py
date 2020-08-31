# Creating class Author
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    #publish method
    def publish(self, title):
        #converting the title to lowercase
        title=title.lower()

        #checking for duplicate books
        if  title in self.books:
             print('The book is already in the books given, No duplicate allowed')
        #if no duplicate books found then the books is added
        else:
              self.books.append(title)
                    
         
            
             


    #_str_ method checking to see if the author has got boobks published
    def __str__(self):
        if self.books:
            titles = ', '.join(self.books)
        else:
            titles = 'No books published'
        return f'Name:{self.name}. Books:{titles}' 

#main method
def main():
    #adding author name and books they published
    Crichton = Author('Michael Crichton')
    Crichton.publish('Sphere')
    Crichton.publish('Prey')
    Crichton.publish('Timeline')
    print(Crichton)

    Banks = Author('Lain M Banks')
    Banks.publish('The State of the Art')
    Banks.publish('Excession')
    Banks.publish('Look to Windward')
    Banks.publish('Surface Detail')
    Banks.publish('Surface Detail')
    print(Banks)

    Naipaul = Author('V.S. Naipaul')
    Naipaul.publish('Half a Life')
    Naipaul.publish('The Masque of Africa')
    Naipaul.publish('The novel Magic Seeds')
    Naipaul.publish('THE NOVEL MAGIC SEEDS')
    print(Naipaul)

    Ahmed = Author('Ahmed')
    print(Ahmed)

main()    
