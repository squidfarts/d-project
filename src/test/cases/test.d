/***********************************************************************************
 *                                                                                 *
 * NAME: test.d                                                                    *
 *                                                                                 *
 * AUTHOR: Michael Brockus.                                                        *
 *                                                                                 *
 * CONTACT: <mailto:michael@squidfarts.com>                                        *
 *                                                                                 *
 * NOTICES:                                                                        *
 *                                                                                 *
 * License: MIT                                                                    *
 *                                                                                 *
 ***********************************************************************************/
module test;

import project;


/*
 *  Prototype functions from the external test file.
 */
unittest
{
    assert(true);
}//end of test case

unittest
{
    assert(itWorks() == "It works");
}//end of test case
