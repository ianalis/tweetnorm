#!/usr/bin/env python

import mox
import tweetnorm as tn
import nose.tools as nt

def test_is_oov():
    nt.assert_equal(tn.is_oov('hopeable'), True)
    nt.assert_equal(tn.is_oov('WikiLeaks'), True)
    nt.assert_equal(tn.is_oov('earthquak'), True)
    nt.assert_equal(tn.is_oov('earthquake'), False)
    nt.assert_equal(tn.is_oov('lv'), True)
    nt.assert_equal(tn.is_oov('love'), False)
    nt.assert_equal(tn.is_oov('2morrow'), True)
    nt.assert_equal(tn.is_oov('tomorrow'), False)
    nt.assert_equal(tn.is_oov("can't"), False)
    nt.assert_equal(tn.is_oov('cant'), False)
    nt.assert_equal(tn.is_oov('govt'), True)
    nt.assert_equal(tn.is_oov('government'), False)
    nt.assert_equal(tn.is_oov('lol'), False)
    
def test_normalize_tokenize():
    """normalize() should properly tokenize the text"""
    m = mox.Mox()
    m.StubOutWithMock(tn, "is_oov")
    text_tokens = [["abc", ["abc"]],
                   ["abc abc", ["abc", "abc"]],
                   [" abc ", ["abc"]],
                   ["take-off won't", ["take-off", "won't"]],
                   ["@twitter #twitter twitter.com http://twitter.com", []]]
    for text, tokens in text_tokens:
        for token in tokens:
            tn.is_oov(token).AndReturn(False)
    m.ReplayAll()
    for text, tokens in text_tokens:
        tn.normalize(text)
    m.UnsetStubs()
    m.VerifyAll()