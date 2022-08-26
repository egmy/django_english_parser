from parsimonious.grammar import Grammar
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from.utils import get_plot 
from django.core.files.storage import FileSystemStorage


from . forms import DocumentForm





from . models import Post


# Create your views here.

from .models import Language
  
# Create your views here.
def index(request):

    languages=Language.objects.all
    return render(request,'englishgrammar/index.html',{"languages":languages})
# Added RequestContext
grammar = Grammar(r"""
    Paragraph= (Sentence space Paragraph)/(Conjoinedsentence)/(Sentence)
    Conjoinedsentence=(Sentence space conj space verbPhase declaration)/(Sentence (space conj space Sentence)* declaration)
    Sentence   =  ((aux space)*(nounPhase space verbPhase declaration))/(Interjection (space Sentence)* declaration)
    verbPhase=(Verb space s)/(adverb space Verb space nounPhase)/(Verb space nounPhase (space PrepPhase)*)/(Verb space adjective)/(Verb (space PrepPhase)*)/(Verb)
    nounPhase    = (article space Noun space PrepPhase)/(article space Noun space s)/(article space (adjective space)* nom)/(nom)
    s = (nounPhase space verbPhase)
    nom=  (Noun (space adjective)*)/((pPnoun space)*(adjective space)* Noun)/(pPnoun space Noun)/(Noun)/(adjective space nom)/(article space Noun)
    PrepPhase=(Preposition space Verb (space Noun)*(space time)*)/(Preposition (space nounPhase)* (space PrepPhase)* (space time)*(space adjective)*)
    Preposition= ("on"/"with"/"to"/"about"/"above"/"around"/"but"/"down"/"up"/"in"/"going"/"with")
    pronoun= ("that"/"this"/"me"/"I"/"he"/"her"/"she"/"him"/"That"/"that"/"you"/"He"/"it"/"You")
    pPnoun=("my"/"mine"/"his"/"your")
    conj=("but"/"and"/"because")
    adjective=("cool"/"best"/"favorite"/"stupid"/"poor"/"scary"/"hungry"/"funny"/"crazy"/"confused"/"smart"/"clear"/"bored"/"public"/"bad"/"few"/"important"/"first"/"last"/"good"/"computer"/"grocery"/"sorry"/"so"/"much"/"complex"/"very"
                /"fat"/"angry"/"frightened"/"little"/"huge"/"large"/"red"/"tall"/"good"/"cool"/"some"/"more"/"proud"/"so"/"much"/
                "new"/"nice")
    article   = ("a"/"the"/"and"/"The"/"to"/"A")
    Noun    = ("girlfriend"/"person"/"world"/"life"/"problem"/"fact"/"science"/"week"/"government"/"year"/"bread"/"store"/"What"/"How"/"name"/"report"/"flight"/"Atlanta"/
        "homework"/"child"/"goal"/"cat"/"dog"/"Python"/"mat"/"shorts"/"ball"/"boy"/"bear"/"squirrel"/"Eric"/"tree"/"movie"/"street"/
                "river"/"dad"/"coffee"/"card"/"woman"/"man"/"animal"/"grass"/"car"/"cheese"/"study"/"space"/"life"/"park"/"mom"/
                "mountain"/"ocean"/"state"/"dirt"/"eggs"/"Egg"/"Pepsi"/"California"/"Tennessee"/"Macbook"/"apple"/"toy"/
                "singer"/"actor"/"Memphis"/"Kansas"/"Chick-fil-A")/(pronoun)
    Verb    = ("like"/"hate"/"see"/"saw"/"looked"/"look"/"get"/"have"/"said"/"say"/"make"/"use"/"find"/"call"/"feel"/"work"/"hear"/"hope"/"come"/"talking"/"trying"/"ready"/"eating"/"right"
                /"made"/"tried"/"make"/"trying"/"grocery"/"likes"/"fly"/"prefers"/"hit"/"left"/"do"/"believe"/"might"/"play"
                /"scored"/"saw"/"chased"/"loves"/"love"/"sat"/"is"/"kicked"/"said"/"thought"/"was"/"bites"/"were"/
                "run"/"accept"/"go"/"drive"/"buy"/"read"/"pay"/"study"/"need"/"wanted"/"eat"/"drink"/
                "clean"/"choose"/"need"/"think"/"hate"/"could"/"be"/"wanted"/"see"/"stay"/"shorts")/(aux (space Verb)*(space adjective)*)/(adverb (space Verb)*(space Noun)*(space adjective)*)/(adverb (space PrepPhase)*)
    adverb=("most"/"just"/"how"/"here"/"very"/"not"/"never"/"really"/"always"/"seriously")
    aux=("will"/"Will"/"Can"/"can"/"has"/"Do"/"am"/"Did"/"did"/"How"/"are")
    space= " "
    time=("today"/"yesterday"/"everyday"/"again")
    Interjection="Hello"/"Goodbye"/"hello"/"what"/"What"/"hi"/"Hi"/"Ouch"/"Oh"/"Uh oh"
    declaration=("."/"!"/"?")*
   
    """)


class File():
    def __init__(self,file):
        self.file = file


def home(request):
    _app_name = "English Grammar App"

    if 'submit_sentence'in request.POST:
        sentence1=request.POST['sentence_form']
        sentence=str(grammar.parse(sentence1))
        pos=find_noun(sentence)
        vo=find_verb(sentence)
        art=find_article(sentence)
        adj=find_adjective(sentence)
        adv=find_adverb(sentence)
        pro=find_pronoun(sentence)
        prep=find_preposition(sentence)
        sen=find_senteence(sentence)
        vp=find_verbphase(sentence)
        np=find_nounphase(sentence)
        prep=find_prepphase(sentence)
        inj=find_interjection(sentence)

        product=Post.objects.create(noun=pos, verb=vo, article=art, adjective=adj, adverb=adv, pronoun=pro, preposition=prep, sentence=sen, verbphase=vp, nounphase=np, prepphase=prep, interjection=inj)
        product.noun=pos
        

        product.save()
        context = {
        "product": product,
        "sentence": sentence1
        
    }
        return render(request, 'englishgrammar/home.html', context )

    elif 'submit_file'in request.POST:
        

        file=request.FILES['myfile'].read()
        file=file.decode()
        sentence=str(grammar.parse(file))
        pos=find_noun(sentence)
        vo=find_verb(sentence)
        art=find_article(sentence)
        adj=find_adjective(sentence)
        adv=find_adverb(sentence)
        pro=find_pronoun(sentence)
        prep=find_preposition(sentence)
        sen=find_senteence(sentence)
        vp=find_verbphase(sentence)
        np=find_nounphase(sentence)
        prep=find_prepphase(sentence)
        inj=find_interjection(sentence)

        product=Post.objects.create(noun=pos, verb=vo, article=art, adjective=adj, adverb=adv, pronoun=pro, preposition=prep, sentence=sen, verbphase=vp, nounphase=np, prepphase=prep, interjection=inj)
        

        product.save()
        context = {
        "product": product,
        "sentence": file
        
    }
        return render(request, 'englishgrammar/home.html', context ) 




    return render(request, "englishgrammar/home.html")

def signin(request):

    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']

        user= authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            fname=user.first_name +" "+user.last_name
            return render(request, 'englishgrammar/home.html', {'fname':fname} )

        else:
            messages.error(request, "Incorrect login" )
            return redirect('home')


    return render(request, "englishgrammar/signin.html")
   


def signup(request):
    if request.method== "POST":
        username= request.POST.get("username")
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST['email']
        password = request.POST['password']
        pass2=request.POST['pass2']

        if User.objects.filter (username=username):
            messages.error (request, "Username already exists")

        if password!= pass2:
            messages.error(request, "Passwords do not match")

        myuser=User.objects.create_superuser(username, email, password)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()

        messages.success(request, "Successful creation of account")

        return redirect("signin")


    return render(request, "englishgrammar/signup.html" )

def signout(request):
    logout(request)
    return redirect('signin')




def eval(node):
    
    n=0
    v=0
    ad=0
    art=0
    n=node.count("noun")
    v=node.count("verb")
    adverb=node.count("adverb")
    art=node.count("article")

    return(n)

def find_noun(node): 
    n=0
    n=(node.count("Noun"))
    return n
def find_verb(node):
    n=0
    n=(node.count("Verb"))
    return n
def find_article(node):
    n=0
    n=(node.count("article"))
    return n
def find_adjective(node):
    n=0
    n=(node.count("adjective"))
    return n
def find_adverb(node):
    n=0
    n=(node.count("adverb"))
    return n
def find_pronoun(node):
    n=0
    n=(node.count("pronoun"))
    return n
def find_preposition(node):
    n=0
    n=(node.count("Preposition"))
    return n
def find_senteence(node):
    n=0
    n=(node.count("Sentence"))
    return n
def find_verbphase(node):
    n=0
    n=(node.count("verbPhase"))
    return n
def find_nounphase(node):
    n=0
    n=(node.count("nounPhase"))
    return n
def find_prepphase(node):
    n=0
    n=(node.count("PrepPhase"))
    return n
def find_interjection(node):
    n=0
    n=(node.count("Interjection"))
    return n







    





