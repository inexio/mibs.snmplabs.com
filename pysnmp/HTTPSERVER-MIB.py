#
# PySNMP MIB module HTTPSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/HTTPSERVER-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:31:25 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
internetServer, = mibBuilder.importSymbols("INTERNETSERVER-MIB", "internetServer")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, iso, Counter32, NotificationType, MibIdentifier, Unsigned32, ModuleIdentity, Integer32, ObjectIdentity, IpAddress, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises", "iso", "Counter32", "NotificationType", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Integer32", "ObjectIdentity", "IpAddress", "Counter64", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
httpServer = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 7, 3))
httpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1))
totalBytesSentHighWord = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalBytesSentHighWord.setStatus('mandatory')
totalBytesSentLowWord = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalBytesSentLowWord.setStatus('mandatory')
totalBytesReceivedHighWord = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalBytesReceivedHighWord.setStatus('mandatory')
totalBytesReceivedLowWord = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalBytesReceivedLowWord.setStatus('mandatory')
totalFilesSent = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalFilesSent.setStatus('mandatory')
totalFilesReceived = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalFilesReceived.setStatus('mandatory')
currentAnonymousUsers = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAnonymousUsers.setStatus('mandatory')
currentNonAnonymousUsers = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentNonAnonymousUsers.setStatus('mandatory')
totalAnonymousUsers = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalAnonymousUsers.setStatus('mandatory')
totalNonAnonymousUsers = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalNonAnonymousUsers.setStatus('mandatory')
maxAnonymousUsers = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxAnonymousUsers.setStatus('mandatory')
maxNonAnonymousUsers = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNonAnonymousUsers.setStatus('mandatory')
currentConnections = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentConnections.setStatus('mandatory')
maxConnections = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxConnections.setStatus('mandatory')
connectionAttempts = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionAttempts.setStatus('mandatory')
logonAttempts = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logonAttempts.setStatus('mandatory')
totalOptions = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalOptions.setStatus('mandatory')
totalGets = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalGets.setStatus('mandatory')
totalPosts = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalPosts.setStatus('mandatory')
totalHeads = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalHeads.setStatus('mandatory')
totalPuts = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalPuts.setStatus('mandatory')
totalDeletes = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalDeletes.setStatus('mandatory')
totalTraces = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalTraces.setStatus('mandatory')
totalMove = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalMove.setStatus('mandatory')
totalCopy = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalCopy.setStatus('mandatory')
totalMkcol = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalMkcol.setStatus('mandatory')
totalPropfind = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalPropfind.setStatus('mandatory')
totalProppatch = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalProppatch.setStatus('mandatory')
totalSearch = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalSearch.setStatus('mandatory')
totalLock = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalLock.setStatus('mandatory')
totalUnlock = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalUnlock.setStatus('mandatory')
totalOthers = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalOthers.setStatus('mandatory')
currentCGIRequests = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentCGIRequests.setStatus('mandatory')
currentBGIRequests = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentBGIRequests.setStatus('mandatory')
totalCGIRequests = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalCGIRequests.setStatus('mandatory')
totalBGIRequests = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalBGIRequests.setStatus('mandatory')
maxCGIRequests = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxCGIRequests.setStatus('mandatory')
maxBGIRequests = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxBGIRequests.setStatus('mandatory')
currentBlockedRequests = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentBlockedRequests.setStatus('mandatory')
totalBlockedRequests = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalBlockedRequests.setStatus('mandatory')
totalAllowedRequests = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalAllowedRequests.setStatus('mandatory')
totalRejectedRequests = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalRejectedRequests.setStatus('mandatory')
totalNotFoundErrors = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalNotFoundErrors.setStatus('mandatory')
totalLockedErrors = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalLockedErrors.setStatus('mandatory')
measuredBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: measuredBandwidth.setStatus('mandatory')
currentCALsforAuthenticatedUsers = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentCALsforAuthenticatedUsers.setStatus('mandatory')
maxCALsforAuthenticatedUsers = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxCALsforAuthenticatedUsers.setStatus('mandatory')
totalCALFailedAuthenticatedUser = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalCALFailedAuthenticatedUser.setStatus('mandatory')
currentCALsforSecureConnections = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 49), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentCALsforSecureConnections.setStatus('mandatory')
maxCALsforSecureConnections = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxCALsforSecureConnections.setStatus('mandatory')
totalCALFailedSecureConnection = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalCALFailedSecureConnection.setStatus('mandatory')
mibBuilder.exportSymbols("HTTPSERVER-MIB", totalAllowedRequests=totalAllowedRequests, maxCALsforSecureConnections=maxCALsforSecureConnections, totalLock=totalLock, totalTraces=totalTraces, totalBytesSentLowWord=totalBytesSentLowWord, totalProppatch=totalProppatch, totalCGIRequests=totalCGIRequests, totalFilesSent=totalFilesSent, totalUnlock=totalUnlock, totalBytesReceivedHighWord=totalBytesReceivedHighWord, totalPropfind=totalPropfind, totalRejectedRequests=totalRejectedRequests, maxCALsforAuthenticatedUsers=maxCALsforAuthenticatedUsers, totalCALFailedSecureConnection=totalCALFailedSecureConnection, measuredBandwidth=measuredBandwidth, currentBGIRequests=currentBGIRequests, connectionAttempts=connectionAttempts, maxConnections=maxConnections, totalDeletes=totalDeletes, totalHeads=totalHeads, currentNonAnonymousUsers=currentNonAnonymousUsers, maxNonAnonymousUsers=maxNonAnonymousUsers, httpStatistics=httpStatistics, totalMkcol=totalMkcol, totalBGIRequests=totalBGIRequests, maxBGIRequests=maxBGIRequests, totalNotFoundErrors=totalNotFoundErrors, totalAnonymousUsers=totalAnonymousUsers, totalBytesReceivedLowWord=totalBytesReceivedLowWord, totalSearch=totalSearch, totalLockedErrors=totalLockedErrors, currentBlockedRequests=currentBlockedRequests, totalPosts=totalPosts, maxAnonymousUsers=maxAnonymousUsers, totalFilesReceived=totalFilesReceived, currentCALsforAuthenticatedUsers=currentCALsforAuthenticatedUsers, totalGets=totalGets, totalCALFailedAuthenticatedUser=totalCALFailedAuthenticatedUser, currentCALsforSecureConnections=currentCALsforSecureConnections, totalBytesSentHighWord=totalBytesSentHighWord, totalBlockedRequests=totalBlockedRequests, httpServer=httpServer, logonAttempts=logonAttempts, totalOthers=totalOthers, totalOptions=totalOptions, currentAnonymousUsers=currentAnonymousUsers, totalMove=totalMove, totalCopy=totalCopy, maxCGIRequests=maxCGIRequests, totalNonAnonymousUsers=totalNonAnonymousUsers, currentConnections=currentConnections, currentCGIRequests=currentCGIRequests, totalPuts=totalPuts)