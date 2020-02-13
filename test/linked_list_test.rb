require 'minitest/autorun'
require 'minitest/reporters'
require 'minitest/skip_dsl'

require_relative 'test_helper'


Minitest::Reporters.use! Minitest::Reporters::SpecReporter.new

describe LinkedList do
    # Arrange
    before do
        @list = LinkedList.new
    end

    describe 'initialize' do
        it 'can be created' do

            # Assert
            expect(@list).must_be_kind_of LinkedList
        end
    end

    describe 'add_first & get_first' do
        it 'can add values to an empty list' do
            # Act
            @list.add_first(3)

            # Assert
            expect(@list.get_first).must_equal 3
        end

        it 'will put the last added item to the front of the list' do
            # Act
            @list.add_first(1)
            @list.add_first(2)

            # Assert
            expect(@list.get_first).must_equal 2

            # Act again
            @list.add_first(3)

            # Assert
            expect(@list.get_first).must_equal 3
        end

        it 'will return `nil` for `getFirst` if the list is empty' do

            expect(@list.get_first).must_be_nil
        end
    end

    describe "search" do
        it "can find an element" do
            @list = LinkedList.new
            @list.add_first(3)
            @list.add_first(2)

            expect(@list.search(3)).must_equal true

            expect(@list.search(2)).must_equal true
        end

        it "returns false if the element is not in the list" do
          @list = LinkedList.new
          @list.add_first(3)
          @list.add_first(2)
          expect(@list.search("pasta")).must_equal false
        end

        it "returns false for an empty list" do
          expect(@list.search(3)).must_equal false
        end
    end

    describe "length" do
        it "will return 0 for an empty list" do
            expect(@list.length).must_equal 0
        end

        it "will return the length for nonempty lists" do
            count = 0
            while count < 5
                @list.add_first(count)
                count += 1
                expect(@list.length).must_equal count
            end
        end
    end

    describe "addLast & getLast" do
        it "will add to the front if the list is empty" do
            @list.add_last(1)
            expect(@list.get_first).must_equal 1
        end

        it "will put new items to the rear of the list" do
            @list.add_last(2)
            expect(@list.length).must_equal 1
            expect(@list.get_last).must_equal 2

            @list.add_last(3)
            expect(@list.get_first).must_equal 2
            expect(@list.get_last).must_equal 3
            expect(@list.length).must_equal 2

            @list.add_last(4)
            expect(@list.get_first).must_equal 2
            expect(@list.get_last).must_equal 4
            expect(@list.length).must_equal 3
        end
    end

    describe 'get_at_index' do
        it 'returns nil if the index is outside the bounds of the list' do
            expect(@list.get_at_index(3)).must_be_nil
        end

        it 'can retrieve an item at an index in the list' do
            @list.add_first(1)
            @list.add_first(2)
            @list.add_first(3)
            @list.add_first(4)

            expect(@list.get_at_index(0)).must_equal 4
            expect(@list.get_at_index(1)).must_equal 3
            expect(@list.get_at_index(2)).must_equal 2
            expect(@list.get_at_index(3)).must_equal 1
        end
    end

    describe 'max and min values' do
        it 'returns nil if the list is empty' do
            expect(@list.find_max()).must_be_nil
            expect(@list.find_min()).must_be_nil
        end

        it 'can retrieve the max and min values in the list' do
            count = 0
            while count < 5
                @list.add_first(count)
                expect(@list.find_max).must_equal count
                expect(@list.find_min).must_equal 0
                count += 1
            end

            @list.add_last(100)
            @list.add_first(-12)
            expect(@list.find_max).must_equal 100
            expect(@list.find_min).must_equal(-12)
        end
    end

    describe "delete" do
        it "delete from empty linked list is a no-op" do
            expect(@list.length).must_equal 0
            @list.delete(4)
            expect(@list.length).must_equal 0
        end

        it "can delete valid values from list" do
            @list.add_last(9)
            @list.add_last(10)
            @list.add_first(4)
            @list.add_first(3)
            @list.add_first(2)

            # delete fist node (requires updating head)
            @list.delete(2)
            expect(@list.get_first).must_equal 3
            expect(@list.length).must_equal 4
            expect(@list.get_last).must_equal 10
            expect(@list.find_max).must_equal 10
            expect(@list.find_min).must_equal 3

            # delete last node
            @list.delete(10)
            expect(@list.get_first).must_equal 3
            expect(@list.length).must_equal 3
            expect(@list.get_last).must_equal 9
            expect(@list.find_max).must_equal 9
            expect(@list.find_min).must_equal 3

            # delete fist node (requires updating head)
            @list.delete(4)
            expect(@list.get_first).must_equal 3
            expect(@list.length).must_equal 2
            expect(@list.get_last).must_equal 9
            expect(@list.find_max).must_equal 9
            expect(@list.find_min).must_equal 3
        end
    end

    describe "nth_from_the_end" do
        it 'returns nil if n is outside the bounds of the list' do
            expect(@list.find_nth_from_end(3)).must_be_nil
        end

        it 'can retrieve an item at index n from the end in the list' do
            @list.add_first(1)
            @list.add_first(2)
            @list.add_first(3)
            @list.add_first(4)

            expect(@list.find_nth_from_end(0)).must_equal 1
            expect(@list.find_nth_from_end(1)).must_equal 2
            expect(@list.find_nth_from_end(2)).must_equal 3
            expect(@list.find_nth_from_end(3)).must_equal 4
            expect(@list.find_nth_from_end(4)).must_be_nil
        end
    end

    describe "reverse" do
        it 'can retrieve an item at index n from the end in the list' do
            @list.add_first(4)
            @list.add_first(3)
            @list.add_first(2)
            @list.add_first(1)
            @list.reverse

            expect(@list.find_nth_from_end(0)).must_equal 1
            expect(@list.find_nth_from_end(1)).must_equal 2
            expect(@list.find_nth_from_end(2)).must_equal 3
            expect(@list.find_nth_from_end(3)).must_equal 4
        end
    end
end
