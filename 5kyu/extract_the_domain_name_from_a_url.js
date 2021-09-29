function domainName(url){
    return url.replace(/^https?\:\/\//i, "").replace("www.", "").split('.')[0]
  }
  