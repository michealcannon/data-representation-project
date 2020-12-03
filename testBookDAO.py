from BookDao import bookDao

book1 = {
    
    'price': 12,
    'author': 'jk',
    'title': 'some fantasy book'

}
book2 = {
    
    'price': 999,
    'author': 'mary',
    'title': 'had a little lamb'

}

returnValue = bookDao.create(book1)
print(returnValue)
returnValue = bookDao.create(book2)
print(returnValue)
returnValue = bookDao.getAll()
print(returnValue)
returnValue = bookDao.findById('1') 
print("find By Id")
print(returnValue)
returnValue = bookDao.update(book2)
print(returnValue)
returnValue = bookDao.findById('2')
print(returnValue)
returnValue = bookDao.delete('2')
print(returnValue)
returnValue = bookDao.getAll()
print(returnValue)

